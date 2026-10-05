"""Iterates every item of an offset-paginated list method.

Fern emits pagers only for organizations with pagination enabled on Fern's servers, so
locally generated list methods return one page. Each page asks for the method's own `limit`
maximum (or less, if you pass `limit`), so a short page is the last one.

    for customer in paginate(client.customers.list): ...
    async for invoice in apaginate(async_client.invoices.list, status="paid"): ...
"""

import typing

from ._page_limits import PAGE_LIMITS

T = typing.TypeVar("T")
T_co = typing.TypeVar("T_co", covariant=True)


class _Page(typing.Protocol[T_co]):
    @property
    def data(self) -> typing.Optional[typing.Sequence[T_co]]: ...


def _start(list_page: typing.Callable[..., object], params: typing.Dict[str, typing.Any]) -> typing.Tuple[int, int]:
    """The first offset and the page size. A callable that is not a client list method, such as
    a lambda, gets the smallest maximum of any list method."""
    owner = getattr(list_page, "__self__", None)
    key = f"{type(owner).__module__}.{getattr(list_page, '__name__', '')}"
    maximum = PAGE_LIMITS.get(key, min(PAGE_LIMITS.values()))
    offset = params.pop("offset", None) or 0
    limit = params.pop("limit", None) or maximum
    return offset, min(limit, maximum)


def paginate(list_page: typing.Callable[..., _Page[T]], /, **params: typing.Any) -> typing.Iterator[T]:
    offset, limit = _start(list_page, params)
    while True:
        items = list_page(offset=offset, limit=limit, **params).data or []
        yield from items
        if len(items) < limit:
            return
        offset += len(items)


async def apaginate(
    list_page: typing.Callable[..., typing.Awaitable[_Page[T]]], /, **params: typing.Any
) -> typing.AsyncIterator[T]:
    offset, limit = _start(list_page, params)
    while True:
        items = (await list_page(offset=offset, limit=limit, **params)).data or []
        for item in items:
            yield item
        if len(items) < limit:
            return
        offset += len(items)
