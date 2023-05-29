from faker import Faker
from .find import FindPet
from src.infra.test.pet_repository_spy import PetRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    pet_repo = PetRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # testing inputs
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]

    # testing outputs
    assert response["Success"] is True
    assert response["data"]

    return response
