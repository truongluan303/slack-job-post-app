from datetime import datetime
from http.client import InvalidURL
from typing import Union

import validators
from linkedin.linkedin import LinkedInApplication
from linkedin.linkedin import LinkedInDeveloperAuthentication

from job_boards.base import JobBoard
from job_boards.base import JobInfo


class LinkedIn(JobBoard):
    """
    Represents a LinkedIn job board
    """

    def __init__(self) -> None:
        self._job_board_name = "LinkedIn"

    def get_job_info(self, job: Union[str, int]) -> JobInfo:
        # if `job` is not a URL, try to extract the job ID from the URL.
        if isinstance(job, str):
            url = job
            if not validators.url(url):
                raise InvalidURL()
        response: dict = self._client.get_job(job_id=job)
        return JobInfo(
            title=response.get("position").get("title"),
            company=response.get("company").get("name"),
            description=response.get("descriptionSnippet"),
            is_active=response.get("active"),
            posted_time=datetime.fromtimestamp(response.get("postingTimestamp")),
        )

    def _create_session(self) -> None:
        # Initiate the developer authentication class
        auth = LinkedInDeveloperAuthentication()
        # Pass it to the client.
        self._client: LinkedInApplication = LinkedInApplication(auth)
