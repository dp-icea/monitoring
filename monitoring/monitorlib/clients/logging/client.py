from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class GetLogResponse(object):
    content: str

class LoggingClient(ABC):
    """Client to obtain log from a USSs."""

    def __init__(self):
      pass

    @abstractmethod
    def get_log(self) -> GetLogResponse:
        """Fetch log of USS

        Returns: Required log string
        """
        raise NotImplementedError()