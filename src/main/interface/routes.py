from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface to Routes"""

    @abstractmethod
    def routes(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Define route"""

        raise Exception("Should implement method: route")
