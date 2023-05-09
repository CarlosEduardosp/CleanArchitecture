from abc import ABC, abstractmethod
from typing import List
from src.doman.models import Pets


class PetRepositoryInterface(ABC):

    """ Interface to Pet Repository """

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age:str, user_id: int) -> Pets:
        """ Abstractmethod """

        raise Exception("Method not implementend")

    @abstractmethod
    def select_pet(self, pet_id: int = None,
                   user_id: int = None
                   ) -> List[Pets]:
        """ Abstractmethod """

        raise Exception("Method not implementend")
