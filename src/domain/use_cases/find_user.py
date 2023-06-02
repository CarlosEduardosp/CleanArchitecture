from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models.users import Users


class FindUser(ABC):
    """Interface to findPet use case"""

    @abstractmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("should implement method: by_id ")

    @abstractmethod
    def by_name(cls, user_name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("should implement method: by_name ")

    @abstractmethod
    def by_id_and_by_name(cls, user_id: int, user_name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("should implement method: by_id and by_name ")
