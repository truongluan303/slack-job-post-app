from job_boards.base import JobBoard


class Glassdoor(JobBoard):
    def __init__(self) -> None:
        self._job_board_name = "Glassdoor"
