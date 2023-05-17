from src.infra.config import DBConnectionHandler, Base
from src.infra.repo.pet_repository import PetRepository


def test_criar_banco():

    # criando o banco de dados.
    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)

    data = PetRepository()
    data = data.select_pet(pet_id=1, user_id=808)
    for i in data[0]:
        print(i)
