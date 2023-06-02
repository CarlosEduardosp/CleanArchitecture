from typing import List, Dict
from src.domain.use_cases.find_user import FindUser as FindUsersinterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models.users import Users


class FindUser(FindUsersinterface):
    """Class to define use case Find user"""

    def __init__(self, user_repository: type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select user by id
        :param - user_id
        :return - dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "data": response}

    def by_name(self, user_name: str) -> Dict[bool, List[Users]]:
        """Select user by name
        :param - user_name
        :return - dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=user_name)

        return {"Success": validate_entry, "data": response}

    def by_id_and_by_name(
        self, user_id: int, user_name: str
    ) -> Dict[bool, List[Users]]:
        """Select user by id and by name
        :param - user_id and user_name
        :return - dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(user_name, str)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=user_name)

        return {"Success": validate_entry, "data": response}
