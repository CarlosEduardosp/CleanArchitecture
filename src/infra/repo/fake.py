from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_use(cls):
        """Something"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="kadu", password="1234")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
