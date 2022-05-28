from typing import NoReturn
from job_boards.base import JobBoard, JobInfo


class Glassdoor(JobBoard):
    def __init__(self) -> NoReturn:
        self._job_board_name = "Glassdoor"
