import os


class OSEnvKeys:
    """
    Containing the names of the OS environment keys
    """

    SLACK_BOT_USER_OAUTH_TOKEN = "SLACK_BOT_USER_OAUTH_TOKEN"
    SLACK_SIGNIN_SECRET = "SLACK_SIGNIN_SECRET"
    JOB_POSTING_CHANNEL = "JOB_POSTING_CHANNEL"
    SLACK_TEST_CHANNEL = "SLACK_TEST_CHANNEL"
    TRIDENT_IMG_URL = "TRIDENT_IMG_URL"
    LINKEDIN_IMG_URL = "LINKEDIN_IMG_URL"
    GLASSDOOR_IMG_URL = "GLASSDOOR_IMG_URL"

    @classmethod
    def to_list(cls):
        """Return a list of the OS environment keys"""
        condition = lambda x: not callable(getattr(cls, x)) and not x.startswith("__")
        return [getattr(cls, attr) for attr in dir(cls) if condition(attr)]


# Slack credentials
SLACK_BOT_USER_OAUTH_TOKEN = os.environ.get(OSEnvKeys.SLACK_BOT_USER_OAUTH_TOKEN)
SLACK_SIGNIN_SECRET = os.environ.get(OSEnvKeys.SLACK_SIGNIN_SECRET)

# Slack Channels
JOB_POSTING_CHANNEL = os.environ.get(OSEnvKeys.JOB_POSTING_CHANNEL)
SLACK_TEST_CHANNEL = os.environ.get(OSEnvKeys.JOB_POSTING_CHANNEL)

# Images URLs
TRIDENT_IMG_URL = os.environ.get(OSEnvKeys.TRIDENT_IMG_URL)
LINKEDIN_IMG_URL = os.environ.get(OSEnvKeys.LINKEDIN_IMG_URL)
GLASSDOOR_IMG_URL = os.environ.get(OSEnvKeys.GLASSDOOR_IMG_URL)
