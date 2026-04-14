from faker import Faker
from requests import codes

from soundingcenter.SoundingCenter import Api


def test_user_self(api_as_api: Api):
    assert api_as_api.user_self().status_code == codes.ok


def test_user_self_first_station(api_as_api: Api):
    assert api_as_api.user_self_first_station()


def test_create_flight(api_as_api: Api, faker: Faker):
    assert (
        api_as_api.create_flight(
            api_as_api.user_self_first_station()["data"]["id"],
            "created",
            faker.name(),
            faker.random_int(400, 406),
            faker.name(),
        ).status_code
        == codes.created
    )
