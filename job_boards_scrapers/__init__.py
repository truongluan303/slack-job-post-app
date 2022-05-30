from http.client import InvalidURL
from typing import Optional
from typing import Union

import requests

from job_boards_scrapers.base import JobBoard
from job_boards_scrapers.base import JobInfo


class Glassdoor(JobBoard):
    def __init__(self) -> None:
        self._job_board_name = "Glassdoor"

    def get_job_info(self, job: Union[str, int]) -> JobInfo:
        return super().get_job_info(job)


class LinkedIn(JobBoard):
    """
    Represents a LinkedIn job board
    """

    _VIEW_LINK_PREFIX = "https://www.linkedin.com/jobs/view"

    def __init__(self) -> None:
        self._job_board_name = "LinkedIn"
        self._title_key = "top-card-layout__title"
        self._company_key = "topcard__org-name-link"
        self._time_ago_key = "posted-time-ago__text"
        self._description_key = "description__text"
        self._link_to_job = ""

    def get_job_info(self, job: Union[str, int]) -> Optional[JobInfo]:
        is_direct_view = False
        # Get the URL if the given param is a job ID
        if isinstance(job, int):
            job = f"{self._VIEW_LINK_PREFIX}/{job}/"
            is_direct_view = True
        # check the URL validity
        if requests.head(job).status_code >= 400:
            raise InvalidURL()

        if not is_direct_view:
            is_direct_view = job.startswith(self._VIEW_LINK_PREFIX)

        if is_direct_view:
            job_info = self._extract_from_direct_view(job)
        else:
            job_info = self._extract_from_jobs_list(job)
        return job_info
