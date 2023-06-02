from typing import Dict
from src.domain.use_cases.register_user import RegisterUser as RegisterUserInterface
from src.data.interfaces import user_repository_interface as UserRepository
from src.domain.models import Users


class RegisterUser(RegisterUserInterface):
    """Class to define usercase: Register User"""

    def __init__(self, user_repository: type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Register user use case
        :param - name: person name
               - password: person password
        :return - Dictionary with informations of the process
        """

        response = None
        # validate_entry == True or False
        validade_entry = isinstance(name, str) and isinstance(password, str)

        if validade_entry:  # if validate_entry == True
            response = self.user_repository.insert_user(name, password)

        return {"Success": validade_entry, "Data": response}
