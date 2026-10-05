# The `limit` maximum of each list method in the Alguna API spec, by module and method name.

import typing

PAGE_LIMITS: typing.Dict[str, int] = {
    "alguna.metrics.client.list": 100,
    "alguna.credit_notes.client.list": 100,
    "alguna.customers.client.list": 100,
    "alguna.invoices.client.list": 100,
    "alguna.merchants.client.list": 100,
    "alguna.payments.client.list": 100,
    "alguna.plans.client.list": 100,
    "alguna.bundles.client.list": 100,
    "alguna.products.client.list": 100,
    "alguna.quotes.client.list": 100,
    "alguna.refunds.client.list": 100,
    "alguna.subscriptions.client.list": 100,
    "alguna.tags.client.list": 100,
    "alguna.tax.client.list_calculations": 100,
    "alguna.wallet_grants.client.list": 100,
    "alguna.wallets.client.list": 100,
}
