import pytest
from ravenloft.models import Domain
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_delete_domain():
    domain = Domain.objects.create(name="Lamordia")
    client = APIClient()
    response = client.delete(f"/domains/{domain.id}/")

    assert response.status_code == 204


@pytest.mark.django_db
def test_requires_valid_domain_id():
    client = APIClient()
    response = client.delete("/domains/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Domain matches the given query."
