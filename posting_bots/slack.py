import slack

from config import SLACK_API_TOKEN


class SlackBot:
    def __init__(self) -> None:
        self._client = slack.WebClient(token=SLACK_API_TOKEN)

    def post(self) -> None:
        self._client.chat_postMessage
