from faker import Faker
from src.data.test.register_pet_spy import RegisterPetSpy
from src.infra.test.pet_repository_spy import PetRepositorySpy
from .register_pet_controller import RegisterPetController
from src.presenters.helpers.http_models import HttpRequest


faker = Faker()


def test_route():
    """testing route method in RegisterUseRoute"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    atributtes = {
        "name": faker.name(),
        "specie": "dog",
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=1),
            "user_name": faker.name(),
        },
    }

    response = register_pet_route.routes(HttpRequest(body=atributtes))

    # testing inputs

    assert register_pet_use_case.registry_param["name"] == atributtes["name"]
    assert register_pet_use_case.registry_param["specie"] == atributtes["specie"]
    assert register_pet_use_case.registry_param["age"] == atributtes["age"]
    assert (
        register_pet_use_case.registry_param["user_information"]
        == atributtes["user_information"]
    )

    # testing outputs
    assert response.status_code == 200
    assert "error" not in response.body
