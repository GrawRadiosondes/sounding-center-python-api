from logging import error
from os import getenv
from os.path import dirname, isfile, join

import pytest
from dotenv import load_dotenv
from faker import Faker

from soundingcenter.SoundingCenter import Api


def load_env():
    env_file = join(dirname(__file__), "../.env")

    if not isfile(env_file):
        error("script can not start because .env file is missing")
        exit(1)

    load_dotenv(env_file)


@pytest.fixture(scope="session")
def api_as_public():
    load_env()
    return Api(
        base_url=getenv("SC_API_URL") or "https://localhost/api",
    )


@pytest.fixture(scope="session")
def api_as_admin():
    load_env()
    return Api(
        getenv("SC_API_URL") or "https://localhost/api",
        getenv("SC_ADMIN_USERNAME") or "admin@domain.tld",
        getenv("SC_ADMIN_PASSWORD") or "password",
    )


@pytest.fixture(scope="session")
def api_as_api():
    load_env()
    return Api(
        getenv("SC_API_URL") or "https://localhost/api",
        getenv("SC_API_USERNAME") or "admin@domain.tld",
        getenv("SC_API_PASSWORD") or "password",
    )


@pytest.fixture(scope="session")
def faker() -> Faker:
    return Faker()
