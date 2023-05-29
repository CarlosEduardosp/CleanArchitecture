from faker import Faker
from src.doman.models import Pets

faker = Faker()


def mock_pets() -> Pets:
    """Mocking Pets"""

    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        specie=faker.name(),
        age=faker.random_number(digits=1),
        user_id=2,
    )
