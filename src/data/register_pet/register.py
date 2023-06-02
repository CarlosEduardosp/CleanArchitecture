from typing import Type, Dict, List
from src.domain.use_cases.register_pet import RegisterPet as RegisterPetInterface
from src.data.Find_user.find import FindUser
from src.data.interfaces.pet_repository_interface import PetRepositoryInterface
from src.domain.models.pets import Pets
from src.domain.models.users import Users


class RegisterPet(RegisterPetInterface):
    """Class to define use case: Register Pet"""

    def __init__(
        self, pet_repository: (PetRepositoryInterface), find_user: Type[FindUser]
    ):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registrer Pet"""

        response = None

        # Validating entry and trying to find an user
        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name=name, specie=specie, age=age, user_id=user_information["user_id"]
            )
        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user infos and select user"""

        user_founded = None
        user_param = user_information.keys()

        if "user_id" in user_param and "user_name" in user_param:
            user_founded = self.find_user.by_id_and_by_name(
                user_information["user_id"], user_information["user_name"]
            )

        elif "user_id" not in user_param and "user_name" in user_param:
            user_founded = self.find_user.by_name(user_information["user_name"])

        elif "user_id" in user_param and "user_name" not in user_param:
            user_founded = self.find_user.by_id(user_information["user_id"])

        else:
            return {"Success": False, "Data": None}

        return user_founded
