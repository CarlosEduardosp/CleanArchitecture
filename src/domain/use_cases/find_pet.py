from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models.pets import Pets


class FindPets(ABC):
    """Interface to findPet use case"""

    @abstractmethod
    def by_pet_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("should implement method: by_id ")

    @abstractmethod
    def by_pet_name(cls, pet_name: str) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("should implement method: by_name ")

    @abstractmethod
    def by_pet_id_and_by_pet_name(
        cls, pet_id: int, pet_name: str
    ) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("should implement method: by_id and by_name ")
