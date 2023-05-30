from faker import Faker
from .register import RegisterPet
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test.find_user_spy import FindUserSpy

faker = Faker()


def test_register_pet():
    """testing registry method in register pet"""

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=2),
            "user_name": faker.name(),
        },
    }

    response = register_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # testing inputs
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]
    assert (
        pet_repo.insert_pet_params["user_id"]
        == attributes["user_information"]["user_id"]
    )

    return response
