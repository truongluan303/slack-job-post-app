import os

from config.local_settings import JOB_POSTING_CHANNEL
from config.local_settings import SLACK_SIGNIN_SECRET


class OSEnvKeys:
    """
    Containing the names of the OS environment keys
    """

    SLACK_BOT_USER_OAUTH_TOKEN = "SLACK_BOT_USER_OAUTH_TOKEN"
    SLACK_SIGNIN_SECRET = "SLACK_SIGNIN_SECRET"
    JOB_POSTING_CHANNEL = "JOB_POSTING_CHANNEL"
    SLACK_TEST_CHANNEL = "SLACK_TEST_CHANNEL"
    SLACK_ICON_PATH = "SLACK_ICON_PATH"

    @classmethod
    def to_list(cls):
        """Return a list of the OS environment keys"""
        condition = lambda x: not callable(getattr(cls, x)) and not x.startswith("__")
        return [getattr(cls, attr) for attr in dir(cls) if condition(attr)]


SLACK_BOT_USER_OAUTH_TOKEN = os.environ.get(OSEnvKeys.SLACK_BOT_USER_OAUTH_TOKEN)
SLACK_SIGNIN_SECRET = os.environ.get(OSEnvKeys.SLACK_SIGNIN_SECRET)
JOB_POSTING_CHANNEL = os.environ.get(OSEnvKeys.JOB_POSTING_CHANNEL)
SLACK_TEST_CHANNEL = os.environ.get(OSEnvKeys.JOB_POSTING_CHANNEL)
SLACK_ICON_PATH = os.environ.get(OSEnvKeys.SLACK_ICON_PATH)
