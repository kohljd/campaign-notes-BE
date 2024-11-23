import pytest
from django.utils import dateparse
from rest_framework.test import APIClient
from ravenloft.tests.factories.domain_factory import DomainFactory


@pytest.mark.django_db
def test_get_domain():
    domain = DomainFactory()
    client = APIClient()
    response = client.get(f"/domains/{domain.id}/")
    updated_at = dateparse.parse_datetime(response.data["updated_at"])

    assert response.status_code == 200
    assert response.data["id"] == domain.id
    assert response.data["name"] == domain.name
    assert response.data["domain_lord"] == domain.domain_lord
    assert response.data["notes"] == domain.notes
    assert updated_at == domain.updated_at


@pytest.mark.django_db
def test_requires_valid_domain_id():
    client = APIClient()
    response = client.get("/domains/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Domain matches the given query."
