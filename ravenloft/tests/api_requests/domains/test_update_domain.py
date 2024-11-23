import pytest
from django.utils import dateparse
from rest_framework.test import APIClient
from ravenloft.tests.factories.domain_factory import DomainFactory


@pytest.mark.django_db
def test_update_domain():
    domain = DomainFactory(domain_lord="Someone", notes="spooky")
    client = APIClient()
    body = {
        "domain_lord": "Viktra Mordenheim",
        "notes": "Lookout for radiation in the forest"
    }
    original_updated_at = domain.updated_at
    response = client.patch(f"/domains/{domain.id}/", body)
    updated_at = dateparse.parse_datetime(response.data["updated_at"])

    assert response.status_code == 200
    assert response.data["id"] == domain.id
    assert response.data["domain_lord"] == "Viktra Mordenheim"
    assert response.data["notes"] == "Lookout for radiation in the forest"
    assert updated_at > original_updated_at


@pytest.mark.django_db
def test_requires_valid_domain_id():
    client = APIClient()
    response = client.patch("/domains/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Domain matches the given query."
