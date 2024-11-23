import pytest
from rest_framework.test import APIClient
from ravenloft.tests.factories.domain_factory import DomainFactory


@pytest.mark.django_db
def test_get_all_domains():
    DomainFactory(name="Lamordia")
    DomainFactory(name="Barovia")

    client = APIClient()
    response = client.get("/domains/")

    assert response.status_code == 200
    assert len(response.data) == 2
