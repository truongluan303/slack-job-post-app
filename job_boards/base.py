from dataclasses import dataclass
from typing import Any, NoReturn, Union
from datetime import datetime


class AuthentificationError(Exception):
    def __init__(self, message="Unable to authenticate the API") -> NoReturn:
        super().__init__(message)


@dataclass
class JobInfo:
    title: str = None
    company: str = None
    company_pic: str = None
    description: str = None
    qualification: str = None
    is_active: bool = True
    posted_time: datetime = None
    url: str = None

    def to_dict(self) -> dict:
        pass


class JobBoard:
    """
    A base class to represent a job board. Subclass it!
    """

    """Should be set by subclasses."""
    _job_board_name: str  # The name of the job board
    _client: Any  # The api

    def __init_subclass__(cls) -> None:
        cls._create_session()

    """Should be implemented by subclasses."""

    def get_job_info(self, job: Union[str, int]) -> JobInfo:
        """
        Get the information about a job posting from its URL.

        Args:
            url (str): Either the URL to the job post, or the ID of the job.

        Returns:
            JobInfo: The information about the job post.
        """
        raise NotImplementedError()

    def _create_session(self) -> NoReturn:
        """
        Create the api session.
        """
        raise NotImplementedError()

    @property
    def name(self) -> str:
        """Get the name of the job board."""
        return self._job_board_name
