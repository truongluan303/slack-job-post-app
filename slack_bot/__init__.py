from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import Union

from slack_sdk.web import SlackResponse

from job_boards_scrapers import JobInfo
from slack_bot.slack_poster import SlackPoster


class Color:
    GREEN = "#36a64f"
    BLUE = "#288BA8"
    PURPLE = "#746AB0"
    RED = "#E83845"
    YELLOW = "FFCE30"
    PINK = "#E389B9"


@dataclass
class Attachment:
    mrkdwn_in: List[str]
    color: str


class SlackJobPoster(SlackPoster):
    def post_job(
        self,
        channels: Union[str, List[str]],
        job_info: JobInfo,
    ) -> Optional[List[SlackResponse]]:
        pass
