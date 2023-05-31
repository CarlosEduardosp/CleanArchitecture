from typing import Dict, List
from src.doman.models.users import Users
from src.doman.test.mock_user import mock_users


class FindUserSpy:
    """Class to define usercase: select User"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.by_id_param = {}
        self.by_name_param = {}
        self.by_id_and_name_param = {}

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """select User by id"""

        self.by_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_users()]

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """select User by name"""

        self.by_name_param["name"] = name
        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_users()]

        return {"Success": validate_entry, "Data": response}

    def by_id_and_by_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """select User by id and by name"""

        self.by_name_param["name"] = name
        self.by_id_param["user_id"] = user_id
        self.by_id_and_name_param["name"] = name
        self.by_id_and_name_param["user_id"] = user_id

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = [mock_users()]

        return {"Success": validate_entry, "Data": response}
