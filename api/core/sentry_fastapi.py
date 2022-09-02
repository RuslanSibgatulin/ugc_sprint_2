import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration


def sentry_init():
    sentry_sdk.init(
        integrations=[
            FastApiIntegration(),
        ],
        traces_sample_rate=1.0
    )
