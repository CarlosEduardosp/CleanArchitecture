from faker import Faker
from .find_user_controller import FindUserController
from src.data.test.find_user_spy import FindUserSpy
from src.infra.test.user_repository_spy import UserRepositorySpy
from src.presenters.helpers.http_models import HttpRequest

faker = Faker()


def test_handle():
    """testing handle method"""

    find_use_use_case = FindUserSpy(UserRepositorySpy())
    find_use_controller = FindUserController(find_use_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(digits=1), "user_name": "kadu"}
    )

    response = find_use_controller.routes(http_request)

    # Testing inputs
    assert (
        find_use_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )
    assert (
        find_use_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body
