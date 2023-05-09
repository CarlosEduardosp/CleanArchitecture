from src.doman.models import Pets
from src.infra.entities import Pets as PetModel
from src.infra.config import DBConnectionHandler


class PetRepository:
    """ Class to manage Pet Repository """

    @classmethod
    def insert_pet(cls, name: str, specie: str, age:str, user_id: int) -> Pets:
        """ Insert data in PetRepository entity
        :param  - name: name of the pet
                - specie: Enum with species acepted
                - age: pet age
                - user__id: id of the
        :return - tuple with new pet inserted """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie,
                    age=new_pet.age,
                    user_id=new_pet.user_id
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
