from src.infra.config import DBConnectionHandler, Base
from src.infra.repo.pet_repository import PetRepository


def test_criar_banco():

    # criando o banco de dados.
    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)

