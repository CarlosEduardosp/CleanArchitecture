from abc import ABC, abstractmethod
from src.domain.models import Users
from typing import Dict


class RegisterUser(ABC):
    """Interface to RegisterUser Use case"""

    @abstractmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Case"""

        raise Exception("Should implement method: register")
