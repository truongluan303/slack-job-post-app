import os


class OSEnvironKeys:
    SLACK_API_TOKEN = "SLACK_API_TOKEN"


SLACK_API_TOKEN = os.environ[OSEnvironKeys.SLACK_API_TOKEN]
