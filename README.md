# alguna

The Python SDK for the [Alguna API](https://alguna.com/docs): usage-based billing,
subscriptions, invoicing and payments. It has sync and async clients, typed models (Pydantic v2)
and typed errors, and it retries safely with idempotency keys. The package ships `py.typed`, so
mypy and pyright check your calls. It requires Python 3.10 or later.

## Install

```bash
pip install alguna
```

## Client

Create an API key in the Alguna dashboard under **Settings → Connections → Developers → API keys**.
A key looks like `<key_id>.<key_secret>`. It is a secret: use the SDK only on a server.

`Alguna()` reads the key from `ALGUNA_API_KEY` when you create the client, or takes `api_key`.
Without a key it raises `ValueError` before it sends a request. Each request sends the
`Alguna-Version` that this release was generated against, unless you set `api_version`, and
`User-Agent: alguna-python/<version>`.

```python
from alguna import Alguna

client = Alguna()
sandbox = Alguna(api_key="<key_id>.<key_secret>", base_url="https://api.sandbox.alguna.io")
pinned = Alguna(api_version="2026-04-01")
```

`AsyncAlguna` takes the same arguments and has the same methods, as awaitables. For a proxy,
TLS settings or another transport, pass your own `httpx.Client` (an `httpx.AsyncClient` for
`AsyncAlguna`) as `httpx_client`:

```python
import httpx

from alguna import Alguna

client = Alguna(httpx_client=httpx.Client(proxy="http://proxy.example.com:8080"))
```

## Requests

The client groups methods by resource, such as `client.customers.create(...)` and
`client.invoices.get(...)`. Each method returns a Pydantic model. Money amounts are decimal
strings, such as `"1250.50"`: use `decimal.Decimal`, not `float`.

```python
from decimal import Decimal

from alguna import Alguna

client = Alguna()
customer = client.customers.create(name="Acme Corp", currency="USD")
invoice = client.invoices.get("inv_1")
print(customer.id, Decimal(invoice.total) * 2)
```

With `AsyncAlguna`, await each call:

```python
import asyncio

from alguna import AsyncAlguna


async def main() -> None:
    client = AsyncAlguna()
    customer = await client.customers.get("cus_1")
    print(customer.name)


asyncio.run(main())
```

## Pagination

A list method, such as `client.customers.list()`, returns one page. `paginate` gives every item:
it asks for the largest page that the list method allows, moves the offset, and stops after the
first short page. Filters go through to the list method. `apaginate` does the same for
`AsyncAlguna`: `async for customer in apaginate(client.customers.list): ...`.

```python
from alguna import Alguna, paginate

client = Alguna()

for customer in paginate(client.customers.list, has_active_subscriptions=True):
    print(customer.id, customer.name)

page = client.customers.list(limit=25, offset=0)
print([customer.id for customer in page.data or []])
```

## Idempotency and retries

Every request other than a GET sends an `Idempotency-Key` header. The SDK makes a UUID v4 key
for each call, or uses the `idempotency_key` that you pass. Every retry of the call sends the
same key, so a retry cannot do a write twice. Pass your own key to make it safe to repeat the
whole call, for example after your process restarts.

`client.events.ingest`, `client.credits.check` and `client.credits.track` are different. The
API identifies their work by the request body, so the SDK makes no key for them and still
retries them. The API removes duplicate events by `unique_id`, and `credits.track` draws credit
once for the same `unique_id`s. A key replaces that identity on `credits.track`, so a new key on
each call would make a redelivered batch draw credit twice. An `idempotency_key` that you pass
is sent on every attempt. `credits.check` with `reserve` needs your key, because the key
identifies the hold.

The client retries a request up to 2 times when:

- the status is 408, 429, 502, 503 or 504.
- the status is 409 and the response has `Retry-After`. The API sends this 409 while a request
  with the same key is still running. Any other 409 is a conflict and raises `ConflictError` at once.
- the connection is refused, reset, closed before the response, or times out.

Before a retry, the client waits for the time in `Retry-After` (up to 60 seconds). Without it,
the client backs off exponentially with jitter, starting at 1 second. Set `max_retries` on the
client or for one request; `0` turns retries off. When you cancel an async call, for example
with `asyncio.timeout`, the client does not retry it.

```python
from alguna import Alguna

client = Alguna(max_retries=5)
customer = client.customers.create(name="Acme Corp", currency="USD", idempotency_key="create-acme-2026-04-01")
client.customers.get(customer.id, request_options={"max_retries": 0})
```

## Timeouts

Each attempt times out after 60 seconds, and the client retries a timed-out attempt as above.
Set `timeout`, in seconds, on the client or for one request. If you pass your own `httpx_client`
and no `timeout`, the timeout of your `httpx_client` applies.

```python
from alguna import Alguna

client = Alguna(timeout=10.0)
client.customers.get("cus_1", request_options={"timeout": 5.0})
```

## Errors

An error status raises `alguna.ApiError` or one of its subclasses, with `status_code`, `body`
(the API's error response) and `headers`. `str(error)` is `HTTP <status>: <message>`. The
message is the API's `detail`, else its `title`, else its `message`, else the HTTP status text.
A failure without a response, after the retries, raises the `httpx` exception, such as
`httpx.ConnectError`.

```python
from alguna import Alguna, ApiError, NotFoundError

client = Alguna()

try:
    client.customers.get("cus_missing")
except NotFoundError as error:
    print(error.status_code, error.body.detail)
except ApiError as error:
    print(error)
```

The subclasses are `BadRequestError`, `UnauthorizedError`, `ForbiddenError`, `NotFoundError`,
`ConflictError`, `UnprocessableEntityError`, `TooManyRequestsError`, `InternalServerError`,
`BadGatewayError`, `ServiceUnavailableError` and `GatewayTimeoutError`.

A successful response never raises because of an unexpected body, so a write that the API
completed never looks like a failure. Fields that the SDK does not know stay available on the model.

## Webhooks

Alguna sends webhooks through Svix. Before you trust a payload, verify its signature (the
`svix-id`, `svix-timestamp` and `svix-signature` headers) against the raw request body, with the
[`svix`](https://pypi.org/project/svix/) package and the signing secret of your endpoint.

Each event type has a model, such as `WebhookInvoicePaidPayload`. Its `model_construct` reads
a payload the way the client reads responses, so an event with a field or value that is new to
this SDK does not raise. Payloads have camelCase keys; the models have snake_case fields.

```python
import json
import os

from svix.webhooks import Webhook

from alguna import WebhookInvoicePaidPayload


def on_webhook(raw_body: bytes, headers: dict[str, str]) -> None:
    # Raises svix.webhooks.WebhookVerificationError if the signature is not valid.
    Webhook(os.environ["ALGUNA_WEBHOOK_SECRET"]).verify(raw_body, headers)
    payload = json.loads(raw_body)
    if payload["type"] == "invoice.paid":
        event = WebhookInvoicePaidPayload.model_construct(**payload)
        print(event.data.id, event.data.total)
```

The [webhooks reference](https://alguna.com/docs/api-reference/v2/webhooks) lists every event.

## Reference

[reference.md](reference.md) lists every method, with its parameters and an example. The
[API reference](https://alguna.com/docs/api-reference/v2/overview) describes each endpoint.

## About this repo

Alguna generates this SDK from the Alguna API spec in a private repository. Open an issue here
to report a bug or to ask for a change. Alguna ports code changes to the private repository, so
a pull request here is not merged directly: the change arrives with a later release. For help
with your account, contact support@alguna.io.
