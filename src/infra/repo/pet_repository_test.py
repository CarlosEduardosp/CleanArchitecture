from faker import Faker
from sqlalchemy import text
from .pet_repository import PetRepository
from src.infra.config import DBConnectionHandler

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """ should insert pet in pet table and return it """

    name = faker.name()
    specie = "cat"
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=3)

    try:
        # inserindo dados no banco
        new_pet = pet_repository.insert_pet(name, specie, age, user_id)

    except:
        print('Falha ao inserir Pet')


def test_select_pet():
    """Select in users"""

    engine = db_connection_handler.get_engine()

    try:
        with engine.connect() as connection:
            # select data in pets
            query_user = connection.execute(text(f"SELECT * FROM pets WHERE id={8} ;"))


    except:
        return "Erro"


def test_delete_pet():
    """deleting data in pets"""

    engine = db_connection_handler.get_engine()

    """ deleting data of select in pets """
    with engine.connect() as connection:
        connection.execute(text(f"DELETE FROM pets WHERE id>{0} ;"))
        connection.commit()
