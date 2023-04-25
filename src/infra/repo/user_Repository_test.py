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
    engine = db_connection_handler.get_engine()

    # SQL comands
    new_user = user_repostory.insert_user(name, password)

    with engine.connect() as connection:
        # select data in users
        query_user = connection.execute(
            text(f"SELECT * FROM users WHERE id={new_user.id};")
        ).fetchone()

        # deleting data of select in users
        connection.execute(text(f"DELETE FROM users WHERE id={new_user.id} ;"))
        connection.commit()

    print(new_user)
    print(query_user)

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
