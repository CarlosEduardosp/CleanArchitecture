# pylint: disable=E1101

from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_Repository import UserRepository

faker = Faker()
user_repostory = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """should insert User"""

    name = faker.name()
    password = faker.word()
    # engine = db_connection_handler.get_engine()

    # SQL comands
    new_user = user_repostory.insert_user(name, password)

    assert new_user.name == name
    assert new_user.password == password


def test_select_user():
    """Select in users"""

    engine = db_connection_handler.get_engine()

    with engine.connect() as connection:
        # select data in users
        query_user = connection.execute(text(f"SELECT * FROM users;"))

    for us in query_user:
        print(us.name, us.id)


def test_delete_user():
    """deleting data in users"""

    engine = db_connection_handler.get_engine()

    """ deleting data of select in users """
    with engine.connect() as connection:
        connection.execute(text(f"DELETE FROM users WHERE id>{0} ;"))
        connection.commit()
