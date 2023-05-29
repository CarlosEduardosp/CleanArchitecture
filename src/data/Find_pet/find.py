from typing import List, Dict
from src.doman.use_cases.find_pet import FindPets as FindPetinterface
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.doman.models.pets import Pets


class FindPet(FindPetinterface):
    """Class to define use case Find Pet"""

    def __init__(self, pet_repository: type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by id
        :param - pet_id
        :return - dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "data": response}

    def by_pet_name(self, pet_name: str) -> Dict[bool, List[Pets]]:
        """Select pet by name
        :param - pet_name
        :return - dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_name, str)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_name=pet_name)

        return {"Success": validate_entry, "data": response}

    def by_pet_id_and_by_pet_name(
        self, pet_id: int, pet_name: str
    ) -> Dict[bool, List[Pets]]:
        """Select pet by id and by name
        :param - pet_id and pet_name
        :return - dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(pet_name, str)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, pet_name=pet_name)

        return {"Success": validate_entry, "data": response}
