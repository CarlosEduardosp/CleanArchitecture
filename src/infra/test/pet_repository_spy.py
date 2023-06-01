from typing import List
from src.doman.models import Pets
from src.doman.test.mock_pet import mock_pets


class PetRepositorySpy:
    """Spy to user Repository"""

    def __init__(self):
        self.insert_pet_params = {}
        self.select_pet_params = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Spy to all the attributes"""

        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        return mock_pets()

    def select_pet(self, pet_id: int = None, name: str = None) -> List[Pets]:
        """Spy to all the attributes"""

        self.select_pet_params["pet_id"] = pet_id
        self.select_pet_params["name"] = name

        return mock_pets()