"""`Alguna` and `AsyncAlguna`: the generated clients with the defaults Fern cannot express.

generators.yml moves the generated clients to base_client.py and has Fern write
pass-through subclasses here; this file replaces them. It defaults the API version, reads
ALGUNA_API_KEY when the client is built (Fern reads it once, at import), names the SDK in
User-Agent, and fails with a clear message when there is no key. The parameters repeat the
generated ones so editors and type checkers see them; tests/test_client.py fails if they drift.
"""

import os
import typing
from importlib import metadata

import httpx

from .base_client import Alguna as _GeneratedAlguna
from .base_client import AsyncAlguna as _GeneratedAsyncAlguna
from .core.logging import LogConfig, Logger
from .environment import AlgunaEnvironment

# The Alguna-Version this SDK was generated against.
DEFAULT_API_VERSION = "2026-04-01"

ApiKey = typing.Union[str, typing.Callable[[], str]]


def _api_key(api_key: typing.Optional[ApiKey]) -> ApiKey:
    api_key = api_key or os.environ.get("ALGUNA_API_KEY")
    if not api_key:
        raise ValueError("No API key: pass api_key=... or set the ALGUNA_API_KEY environment variable.")
    return api_key


def _with_user_agent(headers: typing.Optional[typing.Dict[str, str]]) -> typing.Dict[str, str]:
    headers = dict(headers or {})
    if not any(name.lower() == "user-agent" for name in headers):
        try:
            version = metadata.version("alguna")
        except metadata.PackageNotFoundError:
            version = "0.0.0"
        headers["User-Agent"] = f"alguna-python/{version}"
    return headers


class Alguna(_GeneratedAlguna):
    """Client for the Alguna API. `api_key` defaults to ALGUNA_API_KEY and `api_version` to
    the version this SDK was generated against."""

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AlgunaEnvironment = AlgunaEnvironment.PRODUCTION,
        api_version: str = DEFAULT_API_VERSION,
        api_key: typing.Optional[ApiKey] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_version=api_version,
            api_key=_api_key(api_key),
            headers=_with_user_agent(headers),
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )


class AsyncAlguna(_GeneratedAsyncAlguna):
    """Async client for the Alguna API. Takes the arguments of `Alguna`, with an
    `httpx.AsyncClient` and an optional `async_token`."""

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: AlgunaEnvironment = AlgunaEnvironment.PRODUCTION,
        api_version: str = DEFAULT_API_VERSION,
        api_key: typing.Optional[ApiKey] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_version=api_version,
            api_key=_api_key(api_key),
            headers=_with_user_agent(headers),
            async_token=async_token,
            timeout=timeout,
            max_retries=max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )
