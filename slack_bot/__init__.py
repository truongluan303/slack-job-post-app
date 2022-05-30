from typing import List
from typing import Optional
from typing import Union

from slack_sdk.web import SlackResponse

from config import GLASSDOOR_IMG_URL
from config import LINKEDIN_IMG_URL
from config import TRIDENT_IMG_URL
from job_boards_scrapers import JobBoardType
from job_boards_scrapers import JobInfo
from slack_bot.slack_poster import SlackPoster


class Color:
    GREEN = "#36a64f"
    BLUE = "#288BA8"
    PURPLE = "#746AB0"
    RED = "#E83845"
    YELLOW = "FFCE30"
    PINK = "#E389B9"


class SlackJobPoster(SlackPoster):

    # Map a job board to its image url
    _JOB_BOARD_IMG_MAP = {
        JobBoardType.LINKEDIN: LINKEDIN_IMG_URL,
        JobBoardType.GLASSDOOR: GLASSDOOR_IMG_URL,
    }
    # Map a job board to its color
    _JOB_BOARD_COLOR_MAP = {
        JobBoardType.LINKEDIN: Color.BLUE,
        JobBoardType.GLASSDOOR: Color.GREEN,
    }

    def post_job(
        self,
        channels: Union[str, List[str]],
        job_info: JobInfo,
        job_board: str,
    ) -> Optional[List[SlackResponse]]:

        job_attachment = {
            "mrkdwn_in": ["text"],
            "color": self._JOB_BOARD_COLOR_MAP.get(job_board),
            "pretext": job_info.summary,
            "author_name": job_info.title,
            "author_link": job_info.url,
            "author_icon": self._JOB_BOARD_IMG_MAP.get(job_board),
            "title": job_info.company,
            "text": f"```{job_info.description}```",
            "thumb_url": job_info.company_pic_url,
            "footer": f"This job was posted {job_info.posted_time_ago}",
            "footer_icon": TRIDENT_IMG_URL,
            "actions": [
                {
                    "id": "apply button",
                    "type": "button",
                    "name": "Apply",
                    "integration": {
                        "url": job_info.url,
                    },
                }
            ],
        }
        return self.post_message(
            channels=channels,
            message=f"Check out this job on {job_board}!",
            attachments=[job_attachment],
        )
