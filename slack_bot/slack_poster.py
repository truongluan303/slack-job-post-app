import logging
from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from slack import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.web import SlackResponse

from config import SLACK_BOT_USER_OAUTH_TOKEN
from config import SLACK_ICON_PATH


_LOGGER = logging.getLogger(__name__)


class SlackPoster:
    def __init__(self, slack_token=SLACK_BOT_USER_OAUTH_TOKEN):
        self._client = WebClient(token=slack_token)

    def post_message(
        self,
        channels: Union[str, List[str]],
        message: str,
        attachments: List[Dict] = None,
        thread_ts_by_channel: Dict[str, str] = None,
    ) -> Optional[List[SlackResponse]]:

        if isinstance(channels, str):
            channels = [channels]
        if not channels:
            return None

        if attachments:
            for att in attachments:
                att.update(
                    {
                        "footer_icon": SLACK_ICON_PATH,
                        "ts": datetime.now().timestamp(),
                    }
                )
        slack_responses = []
        for channel in channels:
            thread_ts = (
                thread_ts_by_channel.get(channel) if thread_ts_by_channel else None
            )
            try:
                slack_responses.append(
                    self._client.chat_postMessage(
                        channel=channel,
                        text=message,
                        as_user=True,
                        attachments=attachments,
                        thread_ts=thread_ts,
                    )
                )
            except SlackApiError:
                _LOGGER.exception(f"Failed to send message to {channel}")
        return slack_responses
