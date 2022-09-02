from sentry_sdk import init
from sentry_sdk.integrations.fastapi import FastApiIntegration


def sentry_init():
    init(integrations=[FastApiIntegration()], traces_sample_rate=1.0)
