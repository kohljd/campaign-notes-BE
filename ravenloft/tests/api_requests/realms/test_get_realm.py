import pytest
from django.utils import dateparse
from ravenloft.models import Domain
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_domain():
    domain = Domain.objects.create(
        name="Lamordia",
        domain_lord="Someone",
        notes="spooky"
    )
    client = APIClient()
    response = client.get(f"/domains/{domain.id}/")
    updated_at = dateparse.parse_datetime(response.data["updated_at"])

    assert response.status_code == 200
    assert response.data["id"] == domain.id
    assert response.data["name"] == "Lamordia"
    assert response.data["domain_lord"] == "Someone"
    assert response.data["notes"] == "spooky"
    assert updated_at == domain.updated_at


@pytest.mark.django_db
def test_requires_valid_domain_id():
    client = APIClient()
    response = client.get("/domains/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Domain matches the given query."
