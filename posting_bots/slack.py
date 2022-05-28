from typing import NoReturn
from config import SLACK_API_TOKEN
import slack


class SlackBot:
    def __init__(self) -> NoReturn:
        self._client = slack.WebClient(token=SLACK_API_TOKEN)

    def post(self) -> NoReturn:
        self._client.chat_postMessage
