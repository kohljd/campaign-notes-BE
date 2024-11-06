import pytest
from ravenloft.models import Domain
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_get_all_domains():
    Domain.objects.create(name="Lamordia")
    Domain.objects.create(name="Barovia")

    client = APIClient()
    response = client.get("/domains/")

    assert response.status_code == 200
    assert len(response.data) == 2
