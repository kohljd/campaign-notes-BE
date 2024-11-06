import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_domain():
    client = APIClient()
    url = "/domains/"
    data = {
        "name": "Lamordia",
        "domain_lord": "Someone",
        "notes": "spooky"
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["id"] is not None
    assert response.data["name"] == "Lamordia"
    assert response.data["domain_lord"] == "Someone"
    assert response.data["notes"] == "spooky"
    assert response.data["updated_at"] is not None


@pytest.mark.django_db
def test_duplicate_domain_names_prevented():
    client = APIClient()
    url = "/domains/"
    data = {
        "name": "Lamordia",
        "domain_lord": "Someone",
        "notes": "spooky"
    }
    client.post(url, data)
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "name"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == "domain with this name already exists."


@pytest.mark.django_db
def test_domain_name_required():
    client = APIClient()
    url = "/domains/"
    data = {
        "name": "",
        "domain_lord": "Someone",
        "notes": "spooky"
    }
    client.post(url, data)
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "name"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == "This field may not be blank."
