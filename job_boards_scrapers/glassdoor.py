from typing import Union

from job_boards_scrapers import JobInfo
from job_boards_scrapers.base import JobBoard


class Glassdoor(JobBoard):
    def __init__(self) -> None:
        self._job_board_name = "Glassdoor"

    def get_job_info(self, job: Union[str, int]) -> JobInfo:
        return super().get_job_info(job)
