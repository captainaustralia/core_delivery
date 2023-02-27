import pytest
from django.test import Client

from core_delivery.factories import DefaultUserFactory


@pytest.fixture()
def client():
    return Client()


@pytest.fixture()
def default_user():
    return DefaultUserFactory()
