# pylint: disable=E1101

from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(self, name: str, password: str) -> Users:
        """Insert data in user entity
        :param - name - person name
               - password
        :return - tuple with new user inserted
        """

        Insertdata = namedtuple("Users", "id name, password")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Insertdata(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
        return None