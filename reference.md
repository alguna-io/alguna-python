# Reference
## Events
<details><summary><code>client.events.<a href="src/alguna/events/client.py">ingest</a>(...) -> IngestEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ingests a batch of usage events for metering. Accepts up to 100 events per request. Each event must carry a unique `unique_id` for idempotency and may include arbitrary properties used by metric filters and aggregations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, EventItem
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.events.ingest(
    events=[
        EventItem(
            account="cust_01H1VECT",
            event_name="api_call",
            unique_id="evt_abc123",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**events:** `typing.List[EventItem]` — Array of events to ingest. Maximum 100 events per request
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics
<details><summary><code>client.metrics.<a href="src/alguna/metrics/client.py">list</a>(...) -> MetricListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of billable metrics. Supports filtering by event name, aggregation method, aggregation field, and tag IDs. Results can be sorted by name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.metrics.list(
    limit=20,
    offset=0,
    sort="name:asc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aggregation_field:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by aggregation field (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**aggregation_method:** `typing.Optional[typing.Union[ListMetricsRequestAggregationMethodItem, typing.Sequence[ListMetricsRequestAggregationMethodItem]]]` — Filter by aggregation method (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**event_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by event name (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tag IDs (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.<a href="src/alguna/metrics/client.py">create</a>(...) -> MetricResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Defines a new billable metric. A metric specifies the event name, optional filter groups, and aggregation logic that turns raw ingested events into a quantity the billing engine can price against.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, AggregationRequest
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.metrics.create(
    aggregation=AggregationRequest(
        method="count",
    ),
    event_name="api_call",
    name="API Calls",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**aggregation:** `AggregationRequest` — How events are aggregated into a metric value
    
</dd>
</dl>

<dl>
<dd>

**event_name:** `str` — Event name that triggers this metric
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the metric
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the metric
    
</dd>
</dl>

<dl>
<dd>

**filter_groups:** `typing.Optional[typing.List[FilterGroupRequest]]` — Filter groups to apply to events before aggregation
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.List[str]]` — Tag identifiers to associate with this metric
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.<a href="src/alguna/metrics/client.py">get</a>(...) -> MetricResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single billable metric by ID, including its filter groups and aggregation logic.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.metrics.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the metric
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Checkout Sessions
<details><summary><code>client.checkout_sessions.<a href="src/alguna/checkout_sessions/client.py">create</a>(...) -> CheckoutSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a checkout session and returns a browser-safe session token plus a hosted checkout URL. Embed the URL with the Alguna Checkout SDK, or redirect the customer to it directly. The session charges a plan's prices, ad-hoc line items, or a bare amount, and expires after `expires_in_seconds`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.checkout_sessions.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `typing.Optional[str]` — Total amount to charge when neither plan_id nor line_items are provided
    
</dd>
</dl>

<dl>
<dd>

**checkout_intent:** `typing.Optional[CheckoutSessionCreateRequestCheckoutIntent]` — payment charges the customer; vault only collects and stores a payment method. Defaults to payment.
    
</dd>
</dl>

<dl>
<dd>

**client_reference_id:** `typing.Optional[str]` — Your own reference for this checkout (order ID, cart ID). Echoed on the session and the checkout.session.completed webhook.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — ISO 4217 currency code; defaults to the organization currency
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[CheckoutCustomerRequest]` — Details the customer account is created from when checkout completes. When neither this nor customer_id/customer_alias is provided, the embedded checkout collects them from the customer.
    
</dd>
</dl>

<dl>
<dd>

**customer_alias:** `typing.Optional[str]` — Alternative identifier (external ID) for the customer. Used when customer_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Customer the checkout is for. Omit for guest checkout and pass customer instead — the customer account is created when checkout completes.
    
</dd>
</dl>

<dl>
<dd>

**expires_in_seconds:** `typing.Optional[int]` — Session lifetime in seconds (5 minutes to 7 days). Defaults to 86400 (24 hours).
    
</dd>
</dl>

<dl>
<dd>

**legal_entity_id:** `typing.Optional[str]` — Legal entity to bill from. Defaults to the customer's legal entity, falling back to the organization default.
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.List[CheckoutLineItemRequest]]` — Ad-hoc line items to charge instead of a plan. Mutually exclusive with plan_id.
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` — Plan to check out. The session's line items and amount are derived from the plan's prices. Mutually exclusive with line_items.
    
</dd>
</dl>

<dl>
<dd>

**success_url:** `typing.Optional[str]` — URL the customer can be sent to after a successful checkout
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.checkout_sessions.<a href="src/alguna/checkout_sessions/client.py">get</a>(...) -> CheckoutSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current state of a checkout session, including the payment and subscription it created once the customer completes checkout. Poll this endpoint or subscribe to the `checkout.session.completed` webhook event.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.checkout_sessions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the checkout-session
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credit Notes
<details><summary><code>client.credit_notes.<a href="src/alguna/credit_notes/client.py">list</a>(...) -> CreditNoteListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of credit notes for a given customer. The `customer_id` query parameter is required.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credit_notes.list(
    customer_id="cust_01H1VECT",
    limit=20,
    offset=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — Customer ID to list credit notes for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/alguna/credit_notes/client.py">create</a>(...) -> CreditNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a credit note in draft status. Optionally link it to an invoice. Linked paid invoices are supported, and pre-payment credit notes are supported for Alguna-managed invoices in `issued` or `overdue`. Add line items to specify the credited amounts, then apply the credit note to finalize it. Alternatively, set `apply` to create and apply the credit note in one call — the same synchronous flow as calling Apply Credit Note on a draft. Applying alone does not return funds; send `refund` as well to refund the customer, which requires a linked invoice that is paid. If applying fails, the credit note is left in draft and the error identifies it so it can be applied separately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credit_notes.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**apply:** `typing.Optional[bool]` — Apply the credit note as part of creating it, synchronously, exactly as create followed by Apply Credit Note would. Defaults to false, leaving it a draft. If applying fails the credit note remains a draft and the error identifies it, so it can be retried via Apply Credit Note.
    
</dd>
</dl>

<dl>
<dd>

**billing_period_end:** `typing.Optional[datetime.datetime]` — End of the billing period
    
</dd>
</dl>

<dl>
<dd>

**billing_period_start:** `typing.Optional[datetime.datetime]` — Start of the billing period
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Customer the credit note is issued to. Required unless invoice_id is given, in which case it is taken from the invoice; when both are given they must agree.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Credit note description
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[str]` — Linked invoice. Required unless customer_id is given. Pre-payment credit notes are supported only for Alguna-managed invoices in issued or overdue
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.List[CreateCreditNoteLineItemInput]]` — Line items on the credit note
    
</dd>
</dl>

<dl>
<dd>

**refund:** `typing.Optional[CreditNoteRefundRequest]` — Refund the customer as part of applying the credit note. Requires apply and a linked invoice that is paid; omit it to credit the customer without returning funds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/alguna/credit_notes/client.py">get</a>(...) -> CreditNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single credit note by ID, including line items and attachments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credit_notes.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the credit-note
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/alguna/credit_notes/client.py">apply</a>(...) -> CreditNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies a draft credit note. Applying to a paid invoice can optionally trigger a refund to the original payment method or a wallet. Applying to an Alguna-managed invoice in `issued` or `overdue` records a pre-payment credit without issuing a refund. Once applied, the credit note cannot be modified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credit_notes.apply(
    id="id",
    do_refund=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the credit-note
    
</dd>
</dl>

<dl>
<dd>

**do_refund:** `bool` — Whether to issue a refund when applying to a paid invoice
    
</dd>
</dl>

<dl>
<dd>

**refund_destination:** `typing.Optional[ApplyCreditNoteRequestRefundDestination]` — Where to send the refund when refunding a paid invoice
    
</dd>
</dl>

<dl>
<dd>

**wallet_id:** `typing.Optional[str]` — Wallet to refund to when refund_destination is wallet for a paid-invoice refund
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/alguna/credit_notes/client.py">create_from_invoice</a>(...) -> CreditNoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a draft credit note against an invoice, crediting it at the prices and tax it was issued with rather than calculating tax again. Omit `line_items` to credit everything still uncredited on the invoice. Give `line_items` to credit specific invoice lines, each by the `quantity` of units to credit, which may be fractional. Every line here credits an invoice line item; to credit an amount that is not on the invoice, use create-credit-note instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credit_notes.create_from_invoice(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**apply:** `typing.Optional[bool]` — Apply the credit note as part of creating it, synchronously, exactly as create followed by Apply Credit Note would. Defaults to false, leaving it a draft. If applying fails the credit note remains a draft and the error identifies it, so it can be retried via Apply Credit Note.
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.List[CreditInvoiceLineItemInput]]` — Invoice lines to credit and how many units of each. Omit to credit everything still uncredited on the invoice.
    
</dd>
</dl>

<dl>
<dd>

**refund:** `typing.Optional[CreditNoteRefundRequest]` — Refund the customer as part of applying the credit note. Requires apply and an invoice that is paid; omit it to credit the customer without returning funds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credits
<details><summary><code>client.credits.<a href="src/alguna/credits/client.py">check</a>(...) -> CheckCreditsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prices work before it happens and, optionally, reserves credit for it. The request carries no credit amount: describe the work as the events it will produce, and the response's `charges` say what it prices to per metric.

Send `events` alone to get a price with nothing recorded. Send `reserve` to open a hold, then close it with `POST /credits/track`. `"reserve": {}` with `events` holds enough for exactly that work; `"reserve": {"max_quantity": "100000"}` with `event_name` holds a ceiling in metric units. An `Idempotency-Key` is required whenever `reserve` is set. Each metric is held at the rate frozen when the hold opened, and the hold expires after 15 minutes unless `ttl_seconds` asks for longer (maximum 4 hours).

Only credit-gated metrics are accepted: an event feeding no credit-consuming metric is rejected with `422` and belongs on `POST /events`. Insufficient credit returns `200` with `allowed: false`; an `allowed: true` response carrying no `reservation_id` opened no hold.

The SDKs send no automatic `Idempotency-Key` on this call and retry it without one, because a price check records nothing. Send your own key only to open a hold, where it is required and identifies the hold, or to replay a specific response; a retry then sends the same key. The SDKs do not retry a `500`. `409` means the key is bound to a different reservation. Back off on `429`, which also covers a ledger at its concurrent-hold cap.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credits.check(
    account="cust_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account:** `str` — Customer account ID or alias the credits belong to
    
</dd>
</dl>

<dl>
<dd>

**event_name:** `typing.Optional[str]` — The usage event the work will produce. This is what resolves which billable metrics the check is against — you name what you are about to do, not which metric counts it. An event that feeds no credit-consuming metric is rejected with 422 — that usage belongs on POST /events; an event feeding several credit-consuming metrics is checked (and held) against all of them at once. Optional when events carries the sample; required for reserve.max_quantity.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[TrackCreditEvent]]` — A sample of the work about to happen. The response's charges carry what that work would cost per metric, priced exactly as /track would price it. Nothing is recorded and no credit moves — this is how you learn a price without performing the work. With reserve: {}, the hold is sized to exactly these events.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Dict[str, typing.Any]]` — Event properties used to resolve customer-specific filter groups for this check. Not a billing input: this call records nothing.
    
</dd>
</dl>

<dl>
<dd>

**reserve:** `typing.Optional[ReserveCreditsRequest]` — Open a durable hold alongside the check. An object, never a number: send {} to hold enough for exactly the events in this request, or {"max_quantity": "…"} with event_name for an open-ended ceiling in metric units. The old numeric credit-amount form is rejected — the request no longer carries credit amounts anywhere. Omit for a cost-free preflight or quote (no hold is opened). Requires an Idempotency-Key.
    
</dd>
</dl>

<dl>
<dd>

**ttl_seconds:** `typing.Optional[int]` — How long the hold stays open, in seconds. Defaults to 900 (15 minutes) and cannot exceed 14400 (4 hours), the maximum lifetime any hold may reach. Use it for a run that cannot report progress as it goes; a run that can should send partial settlements to /track instead, since each one slides this same TTL forward. Requires reserve. Not part of idempotency identity: a retry under the same Idempotency-Key replays the original hold with its original expires_at, whatever ttl_seconds it now carries.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credits.<a href="src/alguna/credits/client.py">get_reservation</a>(...) -> ReservationStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reports a reservation's current state, what it covers, and every close already committed against it.

`closes` exists for one recovery: a client that has lost its `Idempotency-Key` and cannot reproduce the events it sent can read what already landed, instead of resending and burning twice. This is a read and cannot settle anything. An unknown or foreign token returns `404`, indistinguishably.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credits.get_reservation(
    reservation_id="reservation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**reservation_id:** `str` — Unique identifier for the reservation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credits.<a href="src/alguna/credits/client.py">track</a>(...) -> TrackCreditsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records usage and charges credit for it. The request carries no credit amount: send what happened, and the response's `charges` carry what it priced to per metric, with `totals` as the sum.

Two shapes. A direct draw (`account` + `events`) charges against the account's current credit. A settlement (`reservation_id` + `events` + `close`) closes a hold opened by `/credits/check`, pricing each metric at the rate frozen when the hold opened. One payload can feed several credit-consuming metrics, and the draw is all-or-nothing: a refusal for one metric leaves every metric uncharged.

Events sent here are both metered and charged, so do not also send them to `POST /events`. An event feeding no credit-consuming metric is rejected with `422` and belongs there instead. Insufficient credit returns `200` with `allowed: false`.

The events' own `unique_id`s identify the work, so a resent batch draws once. The SDKs send no automatic `Idempotency-Key` on this call and retry it without one. Send your own key only to replay a specific response; it then replaces the `unique_id`s as the identity, so reuse it when you resend the same work. The SDKs do not retry a `500`. `409` means the identity is bound to different work. Back off on `429`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, TrackCreditEvent
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.credits.track(
    events=[
        TrackCreditEvent(
            event_name="agent_step",
            unique_id="run_88f_step1",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**events:** `typing.List[TrackCreditEvent]` — The usage being recorded, up to 100 events. The amount charged is computed from these against whichever billable metrics count them; there is no credit amount in the request. On a settlement, an empty array with close: true releases the whole reservation, charging nothing, which is the recovery when work is abandoned.
    
</dd>
</dl>

<dl>
<dd>

**account:** `typing.Optional[str]` — Customer account ID or alias; direct-draw mode. Required unless reservation_id is set, where the account comes from the reservation.
    
</dd>
</dl>

<dl>
<dd>

**close:** `typing.Optional[bool]` — Whether this is the final call for the reservation. Required whenever reservation_id is set: there is no safe default, since true would end runs that meant to continue and false would leak reservations until they expire. The reservation also closes on its own if the events consume everything held. Not valid on a direct draw.
    
</dd>
</dl>

<dl>
<dd>

**on_envelope_exceeded:** `typing.Optional[TrackCreditsRequestOnEnvelopeExceeded]` — What to do when a settle cannot be fully covered by credit on a metric that stops at zero — either because it prices past the reservation's authorized hold, or because credit ran out before a late settle arrived. "reject" (the default) refuses the settle, burning and recording nothing. "record" burns what is available and reports the remainder in the charges' overflow, deliberately weakening a hard stop you configured. Reservation-settlement mode only. The refusal body's reason says which condition fired: adding credit resolves coverage_shortfall, but not envelope_exceeded, whose limit is the hold's size.
    
</dd>
</dl>

<dl>
<dd>

**reservation_id:** `typing.Optional[str]` — Reservation token returned by /check, to close it; reservation-settlement mode. Mutually exclusive with account. The events sent alongside are both metered and charged, so do not send them to /events as well.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Portal
<details><summary><code>client.portal.<a href="src/alguna/portal/client.py">create_session</a>(...) -> CustomerPortalSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a short-lived customer portal session and returns a signed URL the customer can use to access their billing portal. Sessions are single-use per token and expire after a short TTL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.portal.create_session()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_details_settings:** `typing.Optional[BillingDetailsSettingsRequest]` — Settings for the billing details section of the customer portal. When omitted, the organization's defaults apply.
    
</dd>
</dl>

<dl>
<dd>

**customer_alias:** `typing.Optional[str]` — Alternative identifier (external ID) for the customer. Used when customer_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Customer ID the portal session is for. Either customer_id or customer_alias must be provided.
    
</dd>
</dl>

<dl>
<dd>

**invoice_list_settings:** `typing.Optional[InvoiceListSettingsRequest]` — Settings for the invoice list section of the customer portal. When omitted, the organization's defaults apply.
    
</dd>
</dl>

<dl>
<dd>

**plan_overview_settings:** `typing.Optional[PlanOverviewSettingsRequest]` — Settings for the plan overview section of the customer portal. When omitted, the organization's defaults apply.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Customers
<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">list</a>(...) -> CustomerListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of customers. Supports filtering by sales owner, customer success manager, tag IDs, active-subscription status, integration IDs, alias, and contact email.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.list(
    alias="ext_customer_1",
    email="john@example.com",
    limit=20,
    offset=0,
    sort="created_at:desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**alias:** `typing.Optional[str]` — Filter by customer alias (external ID)
    
</dd>
</dl>

<dl>
<dd>

**csm_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by customer success manager user ID (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter by contact email address
    
</dd>
</dl>

<dl>
<dd>

**has_active_subscriptions:** `typing.Optional[bool]` — Filter by whether the customer has active subscriptions
    
</dd>
</dl>

<dl>
<dd>

**integration_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by external integration IDs (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sales_owner_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by sales owner user ID (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order. Sortable fields: name, created_at
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tag IDs (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">create</a>(...) -> CustomerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new customer with optional contacts, billing address, aliases, and a required default currency.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.create(
    currency="USD",
    name="Acme Corp",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency:** `str` — ISO 4217 currency code
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the customer
    
</dd>
</dl>

<dl>
<dd>

**aliases:** `typing.Optional[typing.List[str]]` — Alternative identifiers for the customer
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[AddressRequest]` — Customer billing address
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Optional[typing.List[ContactRequest]]` — Customer contacts
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">lookup</a>(...) -> CustomerLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolves an alias to its Alguna customer ID. The `alias` accepts the Alguna account ID, a customer alias, or a connected-account external ID (such as a Stripe customer ID). Returns 404 if no customer in your organization matches. Use this when you hold an external identifier and only need the Alguna ID; to fetch the full customer, use Get a customer instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.lookup(
    alias="cus_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**alias:** `str` — Customer alias to resolve — an Alguna account ID, a customer alias, or a connected-account external ID (such as a Stripe customer ID)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">get</a>(...) -> CustomerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single customer by ID, including contacts, billing address, and tax details (rate, status, country, type, and taxability reason). The `id` path parameter accepts the Alguna account ID, a customer alias, or a connected-account external ID (such as a Stripe customer ID).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">update</a>(...) -> CustomerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing customer. Only the fields provided in the request body are modified. Supplying contacts or aliases replaces the full list. The `id` path parameter accepts the Alguna account ID, a customer alias, or a connected-account external ID (such as a Stripe customer ID).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**aliases:** `typing.Optional[typing.List[str]]` — Alternative identifiers for the customer
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[AddressRequest]` — Customer billing address
    
</dd>
</dl>

<dl>
<dd>

**contacts:** `typing.Optional[typing.List[ContactRequest]]` — Customer contacts. Replaces all existing contacts when provided
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — ISO 4217 currency code
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the customer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">list_connected_accounts</a>(...) -> ConnectedAccountListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the customer's accounts in connected external systems (for example a Stripe customer or a HubSpot company), including the integration each link belongs to, the account's identifier in the external system, and a link to it where available. The `id` path parameter accepts the Alguna account ID, a customer alias, or a connected-account external ID (such as a Stripe customer ID).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.list_connected_accounts(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">create_connected_account</a>(...) -> ConnectedAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links the customer to an account in an external system by recording the integration and the account's identifier in that system. This records the mapping only: it does not create anything in the external system and does not trigger a sync of any data in either direction. The `id` path parameter accepts the Alguna account ID, a customer alias, or an existing connected-account external ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.create_connected_account(
    id="id",
    external_id="cus_abc123",
    integration_id="intg_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `str` — Identifier of the account in the external system
    
</dd>
</dl>

<dl>
<dd>

**integration_id:** `str` — Identifier of the integration to link the account through
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">delete_connected_account</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the link between the customer and an external-system account. This removes the mapping only: it does not delete anything in the external system and does not trigger a sync. The `id` path parameter accepts the Alguna account ID, a customer alias, or an existing connected-account external ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.delete_connected_account(
    id="id",
    connected_account_id="connectedAccountId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**connected_account_id:** `str` — Unique identifier for the connected-account
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">list_entitlements</a>(...) -> EntitlementListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the flattened list of active entitlements across all of the customer's active subscriptions. Each entry is a single entitlement on the current published version of one active subscription. Use the `subscription_id` field on each entry to see which subscription the entitlement comes from. The `id` path parameter accepts the Alguna account ID, a customer alias, or a connected-account external ID (such as a Stripe customer ID).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.list_entitlements(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.customers.<a href="src/alguna/customers/client.py">list_payment_methods</a>(...) -> PaymentMethodListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the customer's saved, active payment methods, newest first, with redacted details only: card brand, last four digits and expiry, or the last four digits of a bank account. `is_default` marks the payment method that auto-pay charges when a subscription has no payment method of its own. Payment methods saved through a checkout session with `checkout_intent: vault` appear here once the customer completes the session. The `id` path parameter accepts the Alguna account ID, a customer alias, or a connected-account external ID (such as a Stripe customer ID).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.customers.list_payment_methods(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Insights
<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">ar_aging</a>() -> ArAgingSummaryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the organization-wide receivables position as of now: total open balance, the past-due portion, invoice counts, and a breakdown by days past due. Unlike the other insights endpoints this is a point-in-time snapshot rather than a period aggregate, so it takes no date range. Amounts from every currency are converted into the organization's base currency.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.ar_aging()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">ar_aging_by_customer</a>(...) -> ArAgingByCustomerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one entry per customer and currency, each with the open balance, invoice counts, and a breakdown by days past due. A customer billed in more than one currency produces one entry per currency, so entries for a single customer can be summed by invoice count but never by amount. Like the aging summary, this is a point-in-time snapshot and takes no date range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.ar_aging_by_customer(
    customer_alias="ext_39003209203023902",
    customer_id="cust_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_alias:** `typing.Optional[str]` — Filter by an alternative identifier (external ID) for the customer. Used when customer_id is not provided.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter by customer ID. Provide at most one of customer_id or customer_alias; omit both to report on every customer.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">billings_by_customer</a>(...) -> BillingsByCustomerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns top customers ranked by net billings for the selected period, with a comparison to the prior period. Remaining customers are aggregated into an 'other' total.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.billings_by_customer(
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `BillingsByCustomerInsightsRequestDateRange` — Time period for the query. Determines the primary period and automatically calculates a comparison period.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">billings_by_product</a>(...) -> BillingsByProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns billings broken down by product for the selected period, with a comparison to the prior period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.billings_by_product(
    customer_id="cust_abc123",
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `BillingsByProductInsightsRequestDateRange` — Time period for the query.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Optional customer ID to filter by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">billings_over_time</a>(...) -> AmountsOverTimeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a time series of net billings data points split into fixed and metered components. Based on issued invoices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.billings_over_time(
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `BillingsOverTimeInsightsRequestDateRange` — Time period for the query. Determines the primary period and automatically calculates a comparison period.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">customers</a>() -> CustomerInsightsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns customer lifecycle metrics: active, churned, new, and reactivated customer counts with comparison to the prior period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.customers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">customers_over_time</a>(...) -> CustomerInsightsOverTimeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a time series of customer lifecycle events: new, reactivated, existing, and churned customer counts per period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.customers_over_time(
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `CustomersOverTimeInsightsRequestDateRange` — Time period for the query. Determines the primary period and automatically calculates a comparison period.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">revenue</a>() -> NetRevenueResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a net revenue summary including current month, last month, and annualized figures broken down by fixed (recurring) and metered (usage-based) revenue.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.revenue()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">revenue_breakdown_over_time</a>(...) -> RevenueBreakdownOverTimeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a time series of revenue classified by movement type: existing, new, expansion, contraction, and churn.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.revenue_breakdown_over_time(
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `RevenueBreakdownOverTimeInsightsRequestDateRange` — Time period for the query. Determines the primary period and automatically calculates a comparison period.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">revenue_by_customer</a>(...) -> RevenueByCustomerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns top customers ranked by net revenue for the selected period, with a comparison to the prior period. Remaining customers are aggregated into an 'other' total.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.revenue_by_customer(
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `RevenueByCustomerInsightsRequestDateRange` — Time period for the query. Determines the primary period and automatically calculates a comparison period.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">revenue_by_product</a>(...) -> RevenueByProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns revenue broken down by product for the selected period, with a comparison to the prior period.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.revenue_by_product(
    customer_id="cust_abc123",
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `RevenueByProductInsightsRequestDateRange` — Time period for the query.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Optional customer ID to filter by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">revenue_over_time</a>(...) -> AmountsOverTimeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a time series of net revenue data points split into fixed and metered components. Resolution (daily or monthly) is automatically determined by the date range.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.revenue_over_time(
    date_range="this_month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_range:** `RevenueOverTimeInsightsRequestDateRange` — Time period for the query. Determines the primary period and automatically calculates a comparison period.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.insights.<a href="src/alguna/insights/client.py">revenue_by_subscription</a>(...) -> RevenueBySubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the monthly recurring revenue (MRR), annual recurring revenue (ARR), and annual contract value (ACV) for a single subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.insights.revenue_by_subscription(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Integrations
<details><summary><code>client.integrations.<a href="src/alguna/integrations/client.py">list</a>(...) -> IntegrationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the organization's connected integrations (for example Stripe, HubSpot, or QuickBooks). Use the `id` of an integration when linking a connected account to a customer. Supports filtering by provider type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.integrations.list(
    provider="stripe",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Filter by integration provider
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/alguna/integrations/client.py">get</a>(...) -> IntegrationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single integration by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.integrations.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the integration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoices
<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">list</a>(...) -> InvoiceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of invoices. Supports filtering by status, customer, subscription, autopay flag, external reference, tag IDs, and date ranges on invoicing, issue, due, and paid dates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment
import datetime

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.list(
    customer_id="cust_abc123",
    due_date_gte=datetime.datetime.fromisoformat("2026-01-01T00:00:00+00:00"),
    due_date_lte=datetime.datetime.fromisoformat("2026-12-31T00:00:00+00:00"),
    invoicing_date_gte=datetime.datetime.fromisoformat("2026-01-01T00:00:00+00:00"),
    invoicing_date_lte=datetime.datetime.fromisoformat("2026-12-31T00:00:00+00:00"),
    issue_date_gte=datetime.datetime.fromisoformat("2026-01-01T00:00:00+00:00"),
    issue_date_lte=datetime.datetime.fromisoformat("2026-12-31T00:00:00+00:00"),
    limit=20,
    offset=0,
    paid_date_gte=datetime.datetime.fromisoformat("2026-01-01T00:00:00+00:00"),
    paid_date_lte=datetime.datetime.fromisoformat("2026-12-31T00:00:00+00:00"),
    reference="INV-0001",
    sort="created_at:desc",
    subscription_id="sub_abc123",
    tax_calculation_id="taxcalc_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**autopay:** `typing.Optional[bool]` — Filter by autopay flag
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter by customer ID
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[datetime.datetime]` — Due date lower bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[datetime.datetime]` — Due date upper bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**external_reference:** `typing.Optional[str]` — Filter by external reference
    
</dd>
</dl>

<dl>
<dd>

**invoicing_date_gte:** `typing.Optional[datetime.datetime]` — Invoicing date lower bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**invoicing_date_lte:** `typing.Optional[datetime.datetime]` — Invoicing date upper bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gte:** `typing.Optional[datetime.datetime]` — Issue date lower bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lte:** `typing.Optional[datetime.datetime]` — Issue date upper bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**paid_date_gte:** `typing.Optional[datetime.datetime]` — Paid date lower bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**paid_date_lte:** `typing.Optional[datetime.datetime]` — Paid date upper bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Filter by invoice reference number
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order. Sortable fields: created_at, invoicing_date, issue_date, due_date, paid_date, account_name, status
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[ListInvoicesRequestStatusItem, typing.Sequence[ListInvoicesRequestStatusItem]]]` — Filter by invoice status. Pass a comma-separated list to match any.
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` — Filter by subscription ID
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tag IDs (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**tax_calculation_id:** `typing.Optional[str]` — Filter by tax calculation ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">create</a>(...) -> InvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an ad-hoc invoice for a customer. Callers can supply line items, a billing period, purchase order number, and an initial status (`draft` or `issued`). Requesting `issued` releases the invoice for issuance, which completes asynchronously — the response returns the invoice in `processing` and it settles to `issued` shortly after, observable via the Get Invoice endpoint. Alternatively, pass `tax_calculation_id` to turn a persisted tax calculation into an invoice: its line items, tax, and buyer are pinned and the invoice is issued synchronously; add a `payment` and `status: paid` to record settlement and mark it paid in the same call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_period_end:** `typing.Optional[datetime.datetime]` — End of the invoice's billing period, exclusive: for a period through 31 January send 2026-02-01T00:00:00Z. Send with billing_period_start.
    
</dd>
</dl>

<dl>
<dd>

**billing_period_start:** `typing.Optional[datetime.datetime]` — Start of the invoice's billing period, inclusive. Send with billing_period_end.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — ISO 4217 currency code; required unless tax_calculation_id is set
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Existing customer to bill. On the tax_calculation_id path, leave empty to mint a guest customer from the calculation's buyer.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Invoice description or memo
    
</dd>
</dl>

<dl>
<dd>

**issue_date:** `typing.Optional[datetime.datetime]` — Date to issue the invoice
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.List[CreateInvoiceLineItemRequest]]` — Line items to include on the invoice
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Existing sub-merchant the invoice is issued for; you remain the seller of record. Create the merchant before referencing it here. Optional alongside tax_calculation_id, where it must match the merchant the calculation was made for. Requires the merchants entitlement
    
</dd>
</dl>

<dl>
<dd>

**payment:** `typing.Optional[InvoicePaymentRequest]` — Record the customer's already-settled payment and mark the invoice paid in the same call; requires tax_calculation_id
    
</dd>
</dl>

<dl>
<dd>

**purchase_order_number:** `typing.Optional[str]` — Purchase order number
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CreateInvoiceRequestStatus]` — Initial invoice status. Defaults to draft. Setting issued releases the invoice for issuance, which completes asynchronously: the response returns the invoice in processing, and it settles to issued shortly after — poll the Get Invoice endpoint to observe the final status. paid is only valid on the tax_calculation_id path and must be sent together with a payment.
    
</dd>
</dl>

<dl>
<dd>

**tax_calculation_id:** `typing.Optional[str]` — Id of a persisted tax calculation; its stored line items, tax amounts, and buyer become the invoice, which is issued synchronously with no recalculation. Mutually exclusive with line_items (the calculation supplies them). Leave status unset or set it to issued to issue the invoice; set status to paid together with a payment to also mark it paid.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">get</a>(...) -> InvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single invoice by ID, including all line items, totals, and status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">update</a>(...) -> InvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches descriptive metadata on an existing invoice (description, purchase order number). Line items are managed through the dedicated line item endpoints.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Invoice description or memo
    
</dd>
</dl>

<dl>
<dd>

**purchase_order_number:** `typing.Optional[str]` — Purchase order number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">add_line_item</a>(...) -> InvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new line item to an existing invoice. The invoice must not yet be finalized.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.add_line_item(
    id="id",
    description="description",
    quantity="1",
    unit_price="100.00",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — Description of the line item
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `str` — Quantity
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `str` — Unit price, excluding tax. Tax is calculated on top of it.
    
</dd>
</dl>

<dl>
<dd>

**billing_period_end:** `typing.Optional[datetime.datetime]` — End of the service period this line covers, exclusive: for a period through 31 January send 2026-02-01T00:00:00Z. Send with billing_period_start.
    
</dd>
</dl>

<dl>
<dd>

**billing_period_start:** `typing.Optional[datetime.datetime]` — Start of the service period this line covers, inclusive. Send with billing_period_end.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">delete_line_item</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a line item from an invoice. The invoice must not yet be finalized.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.delete_line_item(
    id="id",
    line_item_id="line_item_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `str` — Unique identifier for the line-item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">update_line_item</a>(...) -> LineItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing invoice line item. Only the fields provided in the request body are modified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.update_line_item(
    id="id",
    line_item_id="line_item_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `str` — Unique identifier for the line-item
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the line item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">mark_as_paid</a>(...) -> InvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records a manual payment against an invoice. Accepts an optional amount (defaults to the invoice total), payment date, external payment source, and free-text note. Transitions the invoice to `paid` when the balance is settled.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.mark_as_paid(
    id="id",
    external_payment_source="bank_transfer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**external_payment_source:** `ExternalPaymentSource` — Payment source
    
</dd>
</dl>

<dl>
<dd>

**amount_paid:** `typing.Optional[str]` — Amount paid; defaults to the full invoice total
    
</dd>
</dl>

<dl>
<dd>

**external_payment_note:** `typing.Optional[str]` — Free-text note about the payment
    
</dd>
</dl>

<dl>
<dd>

**paid_date:** `typing.Optional[datetime.datetime]` — Date of payment; defaults to the current date
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">generate_pdf</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the rendered PDF for an invoice as a binary `application/pdf` response. If a custom PDF has been uploaded for the invoice, it is served directly, otherwise the standard template is rendered on demand.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.generate_pdf(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoices.<a href="src/alguna/invoices/client.py">void</a>(...) -> InvoiceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Voids an invoice, marking it as no longer collectable. Accepts an optional void date (defaults to the current date); it may be backdated but must not be in the future or before the invoice's issue date. Only issued or overdue invoices can be voided: voiding an invoice in any other status returns a 400, and an out-of-range void date returns a 422.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.invoices.void(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the invoice
    
</dd>
</dl>

<dl>
<dd>

**void_date:** `typing.Optional[datetime.datetime]` — Date the invoice was voided; defaults to the current date. May be backdated but must not be in the future or before the invoice's issue date.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Merchants
<details><summary><code>client.merchants.<a href="src/alguna/merchants/client.py">list</a>(...) -> MerchantListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of merchants, by display name. Archived merchants are excluded unless you ask for them.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.merchants.list(
    limit=20,
    offset=0,
    sort="display_name:asc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**display_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only merchants with these display names, comma-separated. Matched exactly, including case.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only merchants with these external ids, comma-separated
    
</dd>
</dl>

<dl>
<dd>

**include_archived:** `typing.Optional[bool]` — Include archived merchants, which are excluded by default
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Merchants to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Merchants to skip before the first returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order. Sortable fields: display_name, external_id, support_email, created_at
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/alguna/merchants/client.py">create</a>(...) -> MerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a business you sell on behalf of. Invoices and receipts issued for a merchant carry its name and logo, while your legal entity stays the seller of record and keeps the contract, the payment and the tax liability. A merchant is display identity only: it has no tax or legal configuration of its own.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.merchants.create(
    display_name="Northwind Traders",
    external_id="acct_492",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**display_name:** `str` — Name shown on the documents and emails issued for this merchant
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `str` — Your own identifier for the merchant, unique within your organization.
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[ImageUpload]` — Square mark for places too small for the full logo. We host it and return its URL as avatar_url.
    
</dd>
</dl>

<dl>
<dd>

**logo:** `typing.Optional[ImageUpload]` — Logo shown beside yours in the header of this merchant's documents and emails. We host it and return its URL as logo_url.
    
</dd>
</dl>

<dl>
<dd>

**support_email:** `typing.Optional[str]` — Support address shown to this merchant's buyers. Omit it to show yours instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/alguna/merchants/client.py">get</a>(...) -> MerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single merchant. Archived merchants still resolve, so documents issued before they were archived keep rendering.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.merchants.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/alguna/merchants/client.py">delete</a>(...) -> MerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retires a merchant. Merchants are never deleted, because the documents already issued for them still need their branding: an archived merchant keeps rendering on those, but takes no new attribution — a tax calculation naming it is rejected. Idempotent, and the original archive time is kept. Returns the merchant with `archived_at` set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.merchants.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/alguna/merchants/client.py">update</a>(...) -> MerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a merchant. Only the fields you send are changed: omit a field to leave it alone, send an empty value to clear it. Renames and new branding apply the next time a document is rendered, including documents issued earlier.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.merchants.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the merchant
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `typing.Optional[ImageUpload]` — Replacement square mark. Send it with an empty content to clear the current one.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Name shown on co-branded documents and emails
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[str]` — Your own identifier for the merchant, unique within your organization
    
</dd>
</dl>

<dl>
<dd>

**logo:** `typing.Optional[ImageUpload]` — Replacement logo image. Send it with an empty content to clear the current one.
    
</dd>
</dl>

<dl>
<dd>

**support_email:** `typing.Optional[str]` — Support address shown to this merchant's buyers. Send an empty string to fall back to yours.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.merchants.<a href="src/alguna/merchants/client.py">unarchive</a>(...) -> MerchantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an archived merchant to active use, so new documents can be issued for it again. Idempotent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.merchants.unarchive(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the merchant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payments
<details><summary><code>client.payments.<a href="src/alguna/payments/client.py">list</a>(...) -> PaymentListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of payments. Supports filtering by customer account ID and invoice ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.payments.list(
    customer_id="cust_01H1VECT",
    invoice_id="inv_01H1VECT",
    limit=20,
    offset=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter by customer ID
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[str]` — Filter by invoice ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/alguna/payments/client.py">get</a>(...) -> PaymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single payment by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.payments.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the payment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Plans
<details><summary><code>client.plans.<a href="src/alguna/plans/client.py">list</a>(...) -> PlanListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of plans. Supports filtering by tag IDs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.plans.list(
    limit=20,
    offset=0,
    sort="created_at:desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tag IDs (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/alguna/plans/client.py">create</a>(...) -> PlanResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new plan with its full pricing template — name, currency, contract configuration, and the items (standalone priced products and/or bundles) that subscriptions will inherit. Optional fields cover plan-level discount, spend thresholds, price escalation, entitlements, tags, and invoice/email behavior.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.plans.create(
    currency="USD",
    name="Enterprise Plan",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency:** `str` — ISO 4217 currency code
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Plan name
    
</dd>
</dl>

<dl>
<dd>

**additional_terms:** `typing.Optional[str]` — Markdown additional terms appended to the contract
    
</dd>
</dl>

<dl>
<dd>

**auto_activate:** `typing.Optional[bool]` — Auto-activate subscriptions created from this plan
    
</dd>
</dl>

<dl>
<dd>

**auto_renew:** `typing.Optional[bool]` — Whether the plan auto-renews
    
</dd>
</dl>

<dl>
<dd>

**contract_duration:** `typing.Optional[int]` — Contract duration in months
    
</dd>
</dl>

<dl>
<dd>

**contract_period_type:** `typing.Optional[DurationType]` — Contract period type
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Plan description
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[DiscountInput]` — Plan-level discount applied across the price set
    
</dd>
</dl>

<dl>
<dd>

**entitlements:** `typing.Optional[typing.List[EntitlementInput]]` — Entitlement configs to provision with the plan
    
</dd>
</dl>

<dl>
<dd>

**invoice_settings:** `typing.Optional[CreatePlanInvoiceSettingsInput]` — Invoice/email behavior overrides for the plan
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[CreatePlanItemInput]]` — Items that make up the plan's pricing template. Each item is either a standalone product (product_id + price) or a bundle (bundle_id + name + items).
    
</dd>
</dl>

<dl>
<dd>

**maximum_spend:** `typing.Optional[SpendingThresholdInput]` — Maximum spend per period
    
</dd>
</dl>

<dl>
<dd>

**minimum_spend:** `typing.Optional[SpendingThresholdInput]` — Minimum spend per period
    
</dd>
</dl>

<dl>
<dd>

**payment_terms:** `typing.Optional[str]` — Invoice payment terms
    
</dd>
</dl>

<dl>
<dd>

**price_escalation:** `typing.Optional[PriceEscalationInput]` — Price escalation config
    
</dd>
</dl>

<dl>
<dd>

**renewal_duration:** `typing.Optional[int]` — Renewal duration in months
    
</dd>
</dl>

<dl>
<dd>

**renewal_period_type:** `typing.Optional[DurationType]` — Renewal period type
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Tag IDs to associate with the plan
    
</dd>
</dl>

<dl>
<dd>

**trial_period_days:** `typing.Optional[int]` — Trial period in days
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.plans.<a href="src/alguna/plans/client.py">get</a>(...) -> PlanResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single plan by ID, including its item set and pricing.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.plans.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the plan
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Bundles
<details><summary><code>client.bundles.<a href="src/alguna/bundles/client.py">list</a>(...) -> BundleListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of product bundles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.bundles.list(
    limit=20,
    offset=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bundles.<a href="src/alguna/bundles/client.py">create</a>(...) -> BundleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new product bundle. Product bundles group multiple priced products together so they can be referenced by a single ID in subscriptions, plans, and quotes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, PriceCreateRequest
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.bundles.create(
    name="Standard Plan",
    prices=[
        PriceCreateRequest(
            billing_direction="advance",
            charge_on_contract_start=True,
            fee_type="fixed",
            product_id="product_id",
            type="unit",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the bundle
    
</dd>
</dl>

<dl>
<dd>

**prices:** `typing.List[PriceCreateRequest]` — Prices to include in this bundle
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of the bundle
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bundles.<a href="src/alguna/bundles/client.py">get</a>(...) -> BundleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single product bundle by ID, including its default prices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.bundles.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the bundle
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bundles.<a href="src/alguna/bundles/client.py">update</a>(...) -> BundleResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing product bundle. Supplying `prices` replaces the bundle's full price set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.bundles.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the bundle
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of the bundle
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the bundle
    
</dd>
</dl>

<dl>
<dd>

**prices:** `typing.Optional[typing.List[PriceCreateRequest]]` — Prices to include in this bundle (full replacement)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Products
<details><summary><code>client.products.<a href="src/alguna/products/client.py">list</a>(...) -> ProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of products. Supports filtering by fee type (`fixed` or `metered`), payment terms (`advance` or `arrears`), and associated metric IDs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.products.list(
    limit=20,
    offset=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fee_type:** `typing.Optional[typing.Union[ListProductsRequestFeeTypeItem, typing.Sequence[ListProductsRequestFeeTypeItem]]]` — Filter by fee type (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**metric_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by associated metric IDs (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**payment_terms:** `typing.Optional[typing.Union[ListProductsRequestPaymentTermsItem, typing.Sequence[ListProductsRequestPaymentTermsItem]]]` — Filter by payment terms (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/alguna/products/client.py">create</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new product. Products are the billable unit on subscription items and define whether pricing is fixed or metered, the payment terms, the billing frequency, the SKU for downstream ERP systems, and the revenue allocation method. Metered products must be associated with one or more metrics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.products.create(
    fee_type="fixed",
    name="Platform Fee",
    payment_terms="advance",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fee_type:** `PricingClass` — Whether the product is fixed-price or usage-based
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the product
    
</dd>
</dl>

<dl>
<dd>

**payment_terms:** `BillingDirection` — When the product is billed relative to the billing period. Metered products must be billed in arrears
    
</dd>
</dl>

<dl>
<dd>

**billing_frequency:** `typing.Optional[BillingFrequency]` — How often the product is billed. Required for fixed products; metered products are always recurring
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of the product
    
</dd>
</dl>

<dl>
<dd>

**metric_ids:** `typing.Optional[typing.List[str]]` — Identifiers for metrics to associate with a metered product
    
</dd>
</dl>

<dl>
<dd>

**revenue_allocation_method:** `typing.Optional[RevenueAllocationMethod]` — How revenue is allocated across time periods within a billing cycle
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — Stock keeping unit code used in external ERP or revenue recognition systems
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.List[str]]` — Identifiers for tags to associate with this product
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Canonical (provider-neutral) tax code. Omit for 'general' (standard-rated).
    
</dd>
</dl>

<dl>
<dd>

**unit_label_plural:** `typing.Optional[str]` — Custom plural term for multiple units of the product (e.g. 'API calls'). Falls back to 'units' when omitted
    
</dd>
</dl>

<dl>
<dd>

**unit_label_singular:** `typing.Optional[str]` — Custom singular term for one unit of the product (e.g. 'API call'). Falls back to 'unit' when omitted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/alguna/products/client.py">get</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single product by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.products.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the product
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/alguna/products/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-deletes a product. Products currently used on active subscriptions cannot be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.products.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the product
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/alguna/products/client.py">update</a>(...) -> ProductResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing product. Only the fields provided in the request body are modified.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.products.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the product
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of the product
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the product
    
</dd>
</dl>

<dl>
<dd>

**revenue_allocation_method:** `typing.Optional[RevenueAllocationMethod]` — How revenue is allocated across time periods within a billing cycle
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — Stock keeping unit code used in external ERP or revenue recognition systems
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.List[str]]` — Identifiers for tags to associate with this product
    
</dd>
</dl>

<dl>
<dd>

**tax_code:** `typing.Optional[str]` — Canonical (provider-neutral) tax code. Omit for 'general' (standard-rated).
    
</dd>
</dl>

<dl>
<dd>

**unit_label_plural:** `typing.Optional[str]` — Custom plural term for multiple units of the product (e.g. 'API calls'). Falls back to 'units' when omitted
    
</dd>
</dl>

<dl>
<dd>

**unit_label_singular:** `typing.Optional[str]` — Custom singular term for one unit of the product (e.g. 'API call'). Falls back to 'unit' when omitted
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Quotes
<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">list</a>(...) -> QuoteListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of quotes, filterable by subscription, kind, and status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**kind:** `typing.Optional[ListQuotesRequestKind]` — Filter by quote kind
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of quotes to skip
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListQuotesRequestStatus]` — Filter by document status
    
</dd>
</dl>

<dl>
<dd>

**subscription_id:** `typing.Optional[str]` — Only quotes documenting this subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">create</a>(...) -> QuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a quote, in `draft`. A new-business quote starts from a plan, duplicates an existing subscription using `source_subscription_id`, or starts from a blank canvas with `items` (single phase) or `phases` (ramp); its phases are read and edited under `/quotes/{id}/phases` until the quote is activated. An amendment quote names the active subscription it amends (`amends_subscription_id`) and carries the changed phase in `phases`; it may be issued immediately, so branch on `status` and read `signing_url` when it is present.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.create(
    customer_id="cust_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — Customer ID. For an amendment, must be the subscription's customer.
    
</dd>
</dl>

<dl>
<dd>

**amends_subscription_id:** `typing.Optional[str]` — Amend this active subscription. Takes exactly one entry in phases, with a start_date, and no other origin.
    
</dd>
</dl>

<dl>
<dd>

**auto_activate:** `typing.Optional[bool]` — Whether the subscription takes effect on its own once signed: a new-business quote activates at its contract start, an amendment applies immediately. Defaults to the plan's or organization's setting for new business, and to true for an amendment; each quote keeps its own value.
    
</dd>
</dl>

<dl>
<dd>

**contract:** `typing.Optional[QuoteContractInput]` — Term of the subscription the quote documents. Only valid for a plan-seeded quote.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — When the signing offer lapses. Defaults to the organization's quote expiry window.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[VersionItemInput]]` — Priced items for a single-phase quote. Shorthand for one entry in phases. Prices inherit the customer's currency.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Arbitrary key/value pairs stored on the subscription.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Names the subscription a blank-canvas quote creates. Only valid when neither plan_id nor source_subscription_id is provided; a plan or duplicate names itself.
    
</dd>
</dl>

<dl>
<dd>

**phases:** `typing.Optional[typing.List[QuotePhaseInput]]` — Priced phases in schedule order: the ramp of a blank-canvas quote, or the one changed phase of an amendment. Mutually exclusive with items, plan_id and source_subscription_id.
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` — Seed the quote from a plan. The quote inherits the plan's pricing. Mutually exclusive with source_subscription_id and price_book_id.
    
</dd>
</dl>

<dl>
<dd>

**price_book_id:** `typing.Optional[str]` — Price book a blank-canvas quote draws its pricing from. Mutually exclusive with plan_id and source_subscription_id.
    
</dd>
</dl>

<dl>
<dd>

**source_subscription_id:** `typing.Optional[str]` — Duplicate an existing subscription into a new quote. Mutually exclusive with plan_id and price_book_id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">get</a>(...) -> QuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a quote, including its `signing_url` while a customer signature is pending. Whether the deal is in effect is the state of `subscription_id`, not of the quote: a signed quote stays `signed`, so read that subscription to see activation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">discard</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a draft quote and the draft subscription it documents, for a quote that was abandoned before anyone saw it. Requires `status` of `draft` and a new-business quote: once sent, a quote is a document someone may hold, so it is withdrawn rather than erased.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.discard(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">update</a>(...) -> QuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a quote's name override and its signing deadline. The override names the quote, not the subscription; subscription content is edited through the quote's phases.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**clear_expires_at:** `typing.Optional[bool]` — Make the signing offer open-ended.
    
</dd>
</dl>

<dl>
<dd>

**clear_name:** `typing.Optional[bool]` — Drop the override, falling back to the subscription's name.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — Move the signing deadline. Ignored when clear_expires_at is true.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name override for this quote. Does not rename the subscription. Ignored when clear_name is true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">activate</a>(...) -> QuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Puts a signed quote into effect: requires `status` of `signed`. A new-business quote activates its subscription; an amendment publishes its phase onto the live subscription. Quotes with `auto_activate` take effect on their own once signed (a new-business quote at its contract start), so this is only needed for manual activation. The quote itself stays `signed` — read `subscription_id` to confirm the deal is live.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.activate(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">mark_signed_offline</a>(...) -> QuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Records a signature captured outside the hosted signing page, for consumers that collect signer consent through their own e-sign flow. Accepts a `draft` quote, issuing it first so no live Alguna signing link has to be created for a document signed elsewhere, or one already `sent`. The quote moves to `signed` and the subscription to `accepted`, exactly as a hosted signature would. When issuing a `draft` quote needs approval, the call fails with the pending approval flow and records no signature; after approval issues the quote, call this again with a signature that applies to the issued terms. `signed_at` must lie between the quote's creation and now.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.mark_signed_offline(
    id="id",
    signer_email="ada@acme.com",
    signer_name="Ada Lovelace",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**signer_email:** `str` — Signer's email.
    
</dd>
</dl>

<dl>
<dd>

**signer_name:** `str` — Full name of the signer.
    
</dd>
</dl>

<dl>
<dd>

**signed_at:** `typing.Optional[datetime.datetime]` — When the signer consented, as captured by your e-sign flow. Defaults to now.
    
</dd>
</dl>

<dl>
<dd>

**signer_role:** `typing.Optional[str]` — Signer's job title.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">get_pdf</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the quote document as a binary `application/pdf` response: the PDF the customer signed, or the currently issued one while the quote is out for signature. Returns `404` when there is no issued document — a quote still in `draft`, or a withdrawn amendment, whose staged phase the withdrawal discarded.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.get_pdf(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">list_phases</a>(...) -> QuotePhaseListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the priced phases a quote proposes, in schedule order, each with its revenue totals. An amendment quote has the single phase it was issued for. `sequence` is the position in that order, not an identifier — deleting a phase renumbers the rest, so address a phase by its `id`. Each phase is the subscription version it becomes: once the quote is signed the same rows are readable on the subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.list_phases(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">create_phase</a>(...) -> QuotePhaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stages a further priced phase on a new-business quote that has not been signed. Name its start as a date or as months after the billing start.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, VersionItemInput
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.create_phase(
    id="id",
    items=[
        VersionItemInput()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**request:** `QuotePhaseInput` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">get_phase</a>(...) -> QuotePhaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one of the quote's phases with its revenue totals.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.get_phase(
    id="id",
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**pid:** `str` — Unique identifier for the phase
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">replace_phase</a>(...) -> QuotePhaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the items and start of one of the quote's draft phases. Send the complete item set; items you omit are removed. Phases publish when the quote is sent and cannot change after that.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, VersionItemInput
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.replace_phase(
    id="id",
    pid="pid",
    items=[
        VersionItemInput()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**pid:** `str` — Unique identifier for the phase
    
</dd>
</dl>

<dl>
<dd>

**request:** `QuotePhaseInput` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">delete_phase</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discards one of the quote's draft phases. Phases publish when the quote is sent and cannot be deleted after that.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.delete_phase(
    id="id",
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**pid:** `str` — Unique identifier for the phase
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">list_phase_items</a>(...) -> QuotePhaseItemListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the priced items of one of the quote's phases.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.list_phase_items(
    id="id",
    pid="pid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**pid:** `str` — Unique identifier for the phase
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">send_for_signature</a>(...) -> QuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issues a quote revision (snapshot + rendered PDF) and moves the quote to `sent`, returning it with the `signing_url` for the customer to review and sign. Requires `draft`, `rejected` or `pending_approval`, and only a new-business quote: an amendment is issued when it is created. Omit `signer_email` to send no invitation and share the link yourself. When issuing needs approval, the call fails with the pending approval flow and the quote is not issued until that approval completes; repeating the call meanwhile returns the same pending flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.send_for_signature(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**signer_email:** `typing.Optional[str]` — Email the signing link is sent to. When omitted no email is sent; share signing_url yourself.
    
</dd>
</dl>

<dl>
<dd>

**signer_name:** `typing.Optional[str]` — Name of the person expected to sign, recorded on the signature session.
    
</dd>
</dl>

<dl>
<dd>

**signer_role:** `typing.Optional[str]` — Signer's job title, recorded on the signature session.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.quotes.<a href="src/alguna/quotes/client.py">withdraw</a>(...) -> QuoteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a quote that is out for signature: requires `status` of `sent`. Withdrawing a new-business quote withdraws its subscription and keeps the issued document; withdrawing an amendment discards the staged draft phase, so its document no longer renders. Use Discard a draft quote for one that was never sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.quotes.withdraw(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the quote
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Optional reason recorded on the withdrawal.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Refunds
<details><summary><code>client.refunds.<a href="src/alguna/refunds/client.py">list</a>(...) -> RefundListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of refunds. Supports filtering by status, currency, customer, and payment. Sortable by status, amount, currency, and created date.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.refunds.list(
    currency="USD",
    customer_id="cust_abc123",
    limit=20,
    offset=0,
    payment_id="pay_abc123",
    sort="created_at:desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Filter by ISO 4217 currency code
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter by customer ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `typing.Optional[str]` — Filter by payment ID
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[ListRefundsRequestStatusItem, typing.Sequence[ListRefundsRequestStatusItem]]]` — Filter by refund status. Pass a comma-separated list to match any.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refunds.<a href="src/alguna/refunds/client.py">create</a>(...) -> RefundResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a refund against a payment. For partial or full refunds of invoices, prefer issuing a credit note first via Create Credit Note and applying it, which handles accounting and gives the customer a paper trail. Direct refunds are best for cases where no credit note is needed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.refunds.create(
    amount="99.00",
    payment_id="pay_01H1VECT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `str` — Refund amount
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `str` — The payment to refund
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Reason for the refund
    
</dd>
</dl>

<dl>
<dd>

**statement_descriptor:** `typing.Optional[str]` — Text that appears on the customer's bank statement
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.refunds.<a href="src/alguna/refunds/client.py">get</a>(...) -> RefundResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single refund by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.refunds.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the refund
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Revenue Schedules
<details><summary><code>client.revenue_schedules.<a href="src/alguna/revenue_schedules/client.py">get</a>(...) -> RevenueScheduleReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the revenue schedule for the entire organization, showing projected recognized, deferred, and metered revenue over time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.revenue_schedules.get(
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Target currency for conversion. Uses the entity's default if not specified.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[GetRevenueSchedulesRequestInterval]` — Time interval for schedule entries
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.revenue_schedules.<a href="src/alguna/revenue_schedules/client.py">get_by_customer</a>(...) -> RevenueScheduleReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the aggregated revenue schedule for all of a customer's subscriptions and ad-hoc invoices.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.revenue_schedules.get_by_customer(
    id="id",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the customer
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Target currency for conversion. Uses the entity's default if not specified.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[GetByCustomerRevenueSchedulesRequestInterval]` — Time interval for schedule entries
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.revenue_schedules.<a href="src/alguna/revenue_schedules/client.py">get_by_legal_entity</a>(...) -> RevenueScheduleReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the aggregated revenue schedule for all subscriptions and invoices under a legal entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.revenue_schedules.get_by_legal_entity(
    id="id",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the legal-entity
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Target currency for conversion. Uses the entity's default if not specified.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[GetByLegalEntityRevenueSchedulesRequestInterval]` — Time interval for schedule entries
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.revenue_schedules.<a href="src/alguna/revenue_schedules/client.py">get_by_subscription</a>(...) -> RevenueScheduleReportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the revenue schedule for a single subscription, showing projected recognized, deferred, and metered revenue over time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.revenue_schedules.get_by_subscription(
    id="id",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Target currency for conversion. Uses the entity's default if not specified.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[GetBySubscriptionRevenueSchedulesRequestInterval]` — Time interval for schedule entries
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscription Changes
<details><summary><code>client.subscription_changes.<a href="src/alguna/subscription_changes/client.py">create</a>(...) -> ChangeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Applies a delta (`add`, `remove`, `update`) on top of a source version. The API computes the new version, creates it, and publishes it unless `draft: true` is set. The `effective` field controls when the change takes effect (keyword or specific date). This is the high-level mutation endpoint. See the [Updating a Subscription](https://alguna.com/docs/api-reference/v2/examples/updating-a-subscription) examples for concrete bodies covering price adjustments, plan swaps, bundle operations, and tier replacements.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_changes.create(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateChangeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_changes.<a href="src/alguna/subscription_changes/client.py">preview</a>(...) -> ChangePreviewResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes the same delta as Apply Changes to a Subscription without writing a new version. Use this to drive approval flows or show the customer what is about to change before committing. See the [Updating a Subscription](https://alguna.com/docs/api-reference/v2/examples/updating-a-subscription) examples.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_changes.preview(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateChangeRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscription Versions
<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">list</a>(...) -> SubscriptionPhaseListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every version attached to a subscription: drafts, the currently active published version, and any future pending versions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.list(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">create</a>(...) -> SubscriptionPhaseDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new version from a complete item set. Returns a draft by default that can be edited and published later. This is the snapshot-based mutation path (Path B) for full control over the version contents. For the delta-based alternative, use the Apply Changes to a Subscription endpoint. See the [Updating a Subscription](https://alguna.com/docs/api-reference/v2/examples/updating-a-subscription) examples.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, VersionItemInput
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.create(
    id="id",
    items=[
        VersionItemInput()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[VersionItemInput]` — Complete set of items for this version. Every item must have a full price definition.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Human-readable audit note
    
</dd>
</dl>

<dl>
<dd>

**draft:** `typing.Optional[bool]` — Create as draft (true) or auto-publish (false, default)
    
</dd>
</dl>

<dl>
<dd>

**effective_at:** `typing.Optional[str]` — When the version takes effect (ISO 8601 date, YYYY-MM-DD). Defaults to today.
    
</dd>
</dl>

<dl>
<dd>

**entitlements:** `typing.Optional[typing.List[EntitlementInput]]` — Full entitlement specification for this version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">get_current</a>(...) -> SubscriptionPhaseDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the subscription version that is currently in effect. This is the published version whose start date has passed and whose end date is either in the future or null. Returns 404 if the subscription has no active published version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.get_current(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">get</a>(...) -> SubscriptionPhaseDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single version by ID, including its priced items and entitlements.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.get(
    id="id",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Unique identifier for the version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">replace</a>(...) -> SubscriptionPhaseDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the contents of a draft version in place. Snapshot-based: send the full intended item set. Items you omit are removed. Only draft versions can be replaced, published versions are immutable. See the [Updating a Subscription](https://alguna.com/docs/api-reference/v2/examples/updating-a-subscription) examples.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, VersionItemInput
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.replace(
    id="id",
    vid="vid",
    items=[
        VersionItemInput()
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Unique identifier for the version
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[VersionItemInput]` — Complete replacement set of items for this draft version.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Human-readable audit note
    
</dd>
</dl>

<dl>
<dd>

**effective_at:** `typing.Optional[datetime.date]` — Updated effective date (ISO 8601 date, YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**entitlements:** `typing.Optional[typing.List[EntitlementInput]]` — Full entitlement specification (replaces existing entitlements)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discards an unwanted draft version. Published versions are immutable historical records and cannot be deleted, they must be superseded by creating a new version instead. See the [Updating a Subscription](https://alguna.com/docs/api-reference/v2/examples/updating-a-subscription) examples.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.delete(
    id="id",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Unique identifier for the version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">get_item</a>(...) -> SubscriptionPhaseItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single priced item from a version, addressed by either its product ID or its bundle ID. Bundle items return every child with its price.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.get_item(
    id="id",
    vid="vid",
    ref="ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Unique identifier for the version
    
</dd>
</dl>

<dl>
<dd>

**ref:** `str` — Unique identifier for the item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">publish</a>(...) -> SubscriptionPhaseDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publishes a draft version. If `effective_at` is in the past or today the version becomes the current active version immediately. Otherwise it sits as a pending change on the parent subscription until the effective date. See the [Updating a Subscription](https://alguna.com/docs/api-reference/v2/examples/updating-a-subscription) examples.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.publish(
    id="id",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Unique identifier for the version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscription_versions.<a href="src/alguna/subscription_versions/client.py">get_revenue</a>(...) -> SubscriptionRevenueResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the monthly recurring revenue (MRR), annual recurring revenue (ARR), and annual contract value (ACV) computed from the pricing on the specified subscription version. This is the same calculation used in the Alguna dashboard subscription builder, so results match what is shown there one-to-one.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscription_versions.get_revenue(
    id="id",
    vid="vid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**vid:** `str` — Unique identifier for the version
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Subscriptions
<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">list</a>(...) -> SubscriptionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of subscriptions. Supports filtering by status, customer ID, and tag IDs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.list(
    customer_id="cust_abc123",
    limit=20,
    offset=0,
    sort="created_at:desc",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter by customer ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order. Sortable fields: name, status, created_at, activated_at, ended_at, updated_at, contract_start_date, contract_end_date
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[ListSubscriptionsRequestStatusItem, typing.Sequence[ListSubscriptionsRequestStatusItem]]]` — Filter by subscription status. Pass a comma-separated list to match any.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tag IDs (comma-separated to match any)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">create</a>(...) -> SubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new subscription for a customer. Supports three creation patterns: raw pricing in the request body, from a plan, or from a plan with per-customer overrides. Subscriptions are created in `draft` status and must be activated unless `auto_activate: true` is set. See the [Creating a Subscription](https://alguna.com/docs/api-reference/v2/examples/creating-a-subscription) examples for concrete request bodies and the bundle variants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.create(
    customer_id="cust_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_id:** `str` — Customer ID
    
</dd>
</dl>

<dl>
<dd>

**auto_activate:** `typing.Optional[bool]` — Auto-activate after creation
    
</dd>
</dl>

<dl>
<dd>

**billing:** `typing.Optional[BillingInput]` — Billing configuration
    
</dd>
</dl>

<dl>
<dd>

**contract:** `typing.Optional[ContractInput]` — Contract configuration
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency code. Required when plan_id is not provided. When plan_id is set, defaults to the customer's currency.
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.List[CreateSubscriptionItemInput]]` — Items for the first subscription version. Without plan_id, this is the full set of items. With plan_id, items override matching plan items (by product_id or bundle_id) and non-matching items are appended.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Key-value metadata
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Subscription name
    
</dd>
</dl>

<dl>
<dd>

**plan_id:** `typing.Optional[str]` — Plan ID to use as the base item set (optional)
    
</dd>
</dl>

<dl>
<dd>

**renewal:** `typing.Optional[RenewalInput]` — Renewal configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">get</a>(...) -> SubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single subscription by ID, including the current active version reference and any pending future versions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a draft subscription. Only draft subscriptions can be deleted. Use cancel for subscriptions that have already been activated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">update</a>(...) -> SubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches metadata on a subscription: name, description, trial period, billing flags, subscription-level discount, spending thresholds, price escalation, and tags. This endpoint does not modify the priced item set. To change items, see the [Updating a Subscription](https://alguna.com/docs/api-reference/v2/examples/updating-a-subscription) examples. When an edit of a `sent` subscription saves its terms but the offer is not reissued with them, the call fails with a message that says so and the terms stay saved but cannot be signed; send this request again with an empty body to retry issuing the saved terms.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**billing:** `typing.Optional[UpdateBillingInput]` — Billing configuration
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[DiscountInput]` — Subscription-level discount (percentage only)
    
</dd>
</dl>

<dl>
<dd>

**maximum_spend:** `typing.Optional[SpendingThresholdInput]` — Maximum spend threshold
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Key-value metadata (null value removes key)
    
</dd>
</dl>

<dl>
<dd>

**minimum_spend:** `typing.Optional[SpendingThresholdInput]` — Minimum spend threshold
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Subscription name
    
</dd>
</dl>

<dl>
<dd>

**price_escalation:** `typing.Optional[PriceEscalationInput]` — Price escalation config
    
</dd>
</dl>

<dl>
<dd>

**renewal:** `typing.Optional[RenewalInput]` — Renewal configuration
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — Tag IDs
    
</dd>
</dl>

<dl>
<dd>

**trial_period_days:** `typing.Optional[int]` — Trial period in days
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">activate</a>(...) -> SubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transitions a draft subscription to `active` so it becomes effective for the customer. Idempotent: activating an already-active subscription returns the current state. See the [Creating a Subscription](https://alguna.com/docs/api-reference/v2/examples/creating-a-subscription) examples for the full creation flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.activate(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">get_billing_dates</a>(...) -> BillingDatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current billing cycle range, the list of valid dates for on-cycle version starts, the valid date range for mid-cycle changes, the contract end date, and the next renewal date. Use this to drive date pickers in UI flows that schedule future changes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.get_billing_dates(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">cancel</a>(...) -> SubscriptionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedules a cancellation for a subscription. The `effective` timing can be a keyword (e.g. `immediate`, `end_of_term`) or a specific date. A cancellation reason code is required and a free-text note is optional.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.cancel(
    id="id",
    reason="no_longer_required",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**reason:** `SubscriptionCancelationReason` — Cancellation reason
    
</dd>
</dl>

<dl>
<dd>

**effective:** `typing.Optional[str]` — When cancellation takes effect
    
</dd>
</dl>

<dl>
<dd>

**reason_description:** `typing.Optional[str]` — Additional context for the cancellation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">get_credit_balance</a>(...) -> SubscriptionCreditBalanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the customer's monetary credit balance applicable to this subscription, evaluated at the `as_of` timestamp (defaults to now). Expired grants are excluded from the returned balance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment
import datetime

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.get_credit_balance(
    id="id",
    as_of=datetime.datetime.fromisoformat("2026-04-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**as_of:** `typing.Optional[datetime.datetime]` — Point in time to evaluate the balance at (RFC3339). Defaults to now.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">create_credit_grant</a>(...) -> CreditGrantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a monetary API-granted credit on a subscription. The grant is immediately available for consumption.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.create_credit_grant(
    id="id",
    amount="100.00",
    reason="API promotional credit",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**amount:** `str` — Credit amount to grant
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Reason for the credit grant
    
</dd>
</dl>

<dl>
<dd>

**credit_type:** `typing.Optional[CreditGrantRequestCreditType]` — Type of credit
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — When the credit grant expires
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">list_entitlements</a>(...) -> EntitlementListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every entitlement active on the subscription's current published version, including static boolean/number/string entitlements and grant-based credit allocations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.list_entitlements(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">get_entitlement</a>(...) -> EntitlementResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single active entitlement on a subscription by its entitlement key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.get_entitlement(
    id="id",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` — Unique identifier for the entitlement
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">download_pdf</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the signed contract PDF for a subscription as a binary `application/pdf` response. The document reflects the contract as it was agreed upon with the customer at the point of signing. Returns `404` if the order form was not signed through Alguna and no PDF exists.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.download_pdf(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.subscriptions.<a href="src/alguna/subscriptions/client.py">get_revenue</a>(...) -> SubscriptionRevenueResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the monthly recurring revenue (MRR), annual recurring revenue (ARR), and annual contract value (ACV) for the subscription's current active version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.subscriptions.get_revenue(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the subscription
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tags
<details><summary><code>client.tags.<a href="src/alguna/tags/client.py">list</a>(...) -> TagListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of the organization's tags, sorted by name. Use the returned IDs with the tag_ids filter on list endpoints such as customers, plans, invoices, subscriptions, and metrics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.tags.list(
    limit=20,
    offset=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/alguna/tags/client.py">get</a>(...) -> TagResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single tag by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.tags.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the tag
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tax
<details><summary><code>client.tax.<a href="src/alguna/tax/client.py">list_calculations</a>(...) -> TaxCalculationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of stored calculations, newest first, for reconciling what was quoted against what was issued. Each entry carries the total tax, whether the calculation was issued from and into which invoice, and whether it can still be issued from. Supports filtering by customer reference, currency, issued and expired state, and a tax date range. Per-line tax is on the get endpoint, not here.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment
import datetime

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.tax.list_calculations(
    limit=20,
    offset=0,
    sort="created_at:desc",
    tax_date_gte=datetime.datetime.fromisoformat("2026-01-01T00:00:00+00:00"),
    tax_date_lte=datetime.datetime.fromisoformat("2026-12-31T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**consumed:** `typing.Optional[bool]` — Filter by whether an invoice has been issued from the calculation
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by currency. Pass a comma-separated list to match any.
    
</dd>
</dl>

<dl>
<dd>

**customer_reference:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by your own buyer id. Pass a comma-separated list to match any.
    
</dd>
</dl>

<dl>
<dd>

**expired:** `typing.Optional[bool]` — Filter by whether the calculation can still be issued from
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort field and direction in format field:order. Sortable fields: created_at, tax_date, expires_at, total_tax, currency.
    
</dd>
</dl>

<dl>
<dd>

**tax_date_gte:** `typing.Optional[datetime.datetime]` — Tax date lower bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**tax_date_lte:** `typing.Optional[datetime.datetime]` — Tax date upper bound (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tax.<a href="src/alguna/tax/client.py">create_calculation</a>(...) -> TaxCalculationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Computes tax for inline line items against your legal entity's configured tax engine and stores the result, returning an id (with an expiry) you pass when issuing a receipt to pin these exact line items and amounts. Each call creates a new calculation; send an `Idempotency-Key` header to make a retry return the original calculation instead of a new one. Provide a buyer address (and optional tax ids for reverse-charge / exemption) and per-line canonical tax codes; an omitted code defaults to general business SaaS.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna, TaxCalculationCustomerRequest, TaxCalculationAddressRequest, TaxCalculationLineItemRequest
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.tax.create_calculation(
    currency="USD",
    customer=TaxCalculationCustomerRequest(
        address=TaxCalculationAddressRequest(
            country="USA",
        ),
        first_name="Jane",
        last_name="Doe",
    ),
    line_items=[
        TaxCalculationLineItemRequest(
            amount="100.00",
            quantity="1",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency:** `str` — ISO 4217 currency code
    
</dd>
</dl>

<dl>
<dd>

**customer:** `TaxCalculationCustomerRequest` — Who is being taxed
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.List[TaxCalculationLineItemRequest]` — Line items to tax
    
</dd>
</dl>

<dl>
<dd>

**legal_entity_id:** `typing.Optional[str]` — Selling legal entity; defaults to the org's default when omitted
    
</dd>
</dl>

<dl>
<dd>

**merchant_id:** `typing.Optional[str]` — Existing sub-merchant the receipt is issued for; you remain the seller of record. Create the merchant before referencing it here. Requires the merchants entitlement
    
</dd>
</dl>

<dl>
<dd>

**tax_behavior:** `typing.Optional[TaxBehavior]` — Whether line amounts exclude (default) or already include tax
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tax.<a href="src/alguna/tax/client.py">get_calculation</a>(...) -> TaxCalculationDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one stored calculation: the lines as they were submitted joined with the engine's answer for each, plus the invoice it was issued into when it has been. A calculation stays readable after it expires or is issued from, so this is the audit record behind an invoice's tax. Read it back with the `tax_calculation_id` returned on the invoice.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.tax.get_calculation(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the calculation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Wallet Grants
<details><summary><code>client.wallet_grants.<a href="src/alguna/wallet_grants/client.py">list</a>(...) -> WalletGrantListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of wallet grants across the organization. Supports filtering by wallet ID and grant status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallet_grants.list(
    limit=20,
    offset=0,
    wallet_id="wlt_abc123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListWalletGrantsRequestStatus]` — Filter by grant status
    
</dd>
</dl>

<dl>
<dd>

**wallet_id:** `typing.Optional[str]` — Filter by wallet ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallet_grants.<a href="src/alguna/wallet_grants/client.py">create</a>(...) -> WalletGrantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new grant on a wallet for a given amount. Grants may carry an expiry date and an associated payment reference.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallet_grants.create(
    amount="amount",
    wallet_id="wlt_01H2ABC",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `str` — Amount of the grant
    
</dd>
</dl>

<dl>
<dd>

**wallet_id:** `str` — Identifier of the wallet
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the grant
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` — When the grant expires
    
</dd>
</dl>

<dl>
<dd>

**payment_id:** `typing.Optional[str]` — Associated payment identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallet_grants.<a href="src/alguna/wallet_grants/client.py">get</a>(...) -> WalletGrantResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single wallet grant by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallet_grants.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet-grant
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Wallets
<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">list_grants</a>(...) -> WalletGrantListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every grant attached to a specific wallet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.list_grants(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">list</a>(...) -> WalletListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of wallets. Supports filtering by customer ID and active status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.list(
    customer_id="cust_01H2ABC",
    limit=20,
    offset=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter by active status
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Filter by customer ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">create</a>(...) -> WalletResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new wallet for a customer. Wallets hold a balance in a single currency and can optionally be restricted to a specific set of products.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.create(
    currency="USD",
    customer_id="cust_01H2ABC",
    name="Main Wallet",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency:** `str` — Currency code
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — Identifier of the customer
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name of the wallet
    
</dd>
</dl>

<dl>
<dd>

**product_ids:** `typing.Optional[typing.List[str]]` — Product IDs that can be purchased with this wallet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">get</a>(...) -> WalletResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches a single wallet by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a wallet. Wallets with a non-zero balance cannot be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">update</a>(...) -> WalletResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing wallet. Supports changing the name, currency, active flag, and the list of products the wallet can be used against.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether the wallet is active
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency code
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the wallet
    
</dd>
</dl>

<dl>
<dd>

**product_ids:** `typing.Optional[typing.List[str]]` — Product IDs that can be purchased with this wallet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">get_balance</a>(...) -> WalletBalanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current balance for a wallet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.get_balance(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">credit</a>(...) -> WalletResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Credits a wallet by the specified amount and records the transaction type, reference ID, and optional description on the ledger.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.credit(
    id="id",
    amount="amount",
    reference_id="pay_01H3DEF",
    transaction_type="credit_grant",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreditDebitWalletRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.wallets.<a href="src/alguna/wallets/client.py">debit</a>(...) -> WalletResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Debits a wallet by the specified amount. Fails with `422` if the wallet has insufficient balance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alguna import Alguna
from alguna.environment import AlgunaEnvironment

client = Alguna(
    api_key="<token>",
    api_version="<Alguna-Version>",
    environment=AlgunaEnvironment.PRODUCTION,
)

client.wallets.debit(
    id="id",
    amount="amount",
    reference_id="pay_01H3DEF",
    transaction_type="credit_grant",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier for the wallet
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreditDebitWalletRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

