import pytest
from rest_framework.test import APIClient
pytestmark = pytest.mark.django_db


def test_create_npc():
    client = APIClient()
    url = "/npcs/"
    data = {
        "name": "Aria",
        "appearance": "Mid-30's half-elf woman in commoner clothes",
        "living_status": "Unknown",
        "relationship_to_party": "Friendly",
        "notes": "Met in Neufurchtenburg"
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["id"] is not None
    assert response.data["name"] == data["name"]
    assert response.data["appearance"] == data["appearance"]
    assert response.data["living_status"] == data["living_status"]
    assert response.data["relationship_to_party"] == data["relationship_to_party"]
    assert response.data["notes"] == data["notes"]
    assert response.data["created_at"] is not None
    assert response.data["updated_at"] is not None


def test_default_values():
    client = APIClient()
    url = "/npcs/"
    data = {"name": "Aria"}
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["appearance"] == ""
    assert response.data["living_status"] == "Alive"
    assert response.data["relationship_to_party"] == "Neutral"
    assert response.data["notes"] == ""


def test_required_data():
    """
    Required fields: name
    """
    client = APIClient()
    url = "/npcs/"
    data = {}
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    errors = response.data["errors"]
    assert len(errors) == 1
    assert errors[0]["field"] == "name"

    error_detail = errors[0]["field_errors"][0]["detail"]
    assert error_detail == "This field is required."


def test_invalid_name_length():
    client = APIClient()
    url = "/npcs/"
    data = {"name": "A" * 61}
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "name"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == "Ensure this field has no more than 60 characters."


def test_invalid_living_status():
    client = APIClient()
    url = "/npcs/"
    data = {
        "name": "Aria",
        "living_status": "Invalid Status"
    }
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "living_status"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == '"Invalid Status" is not a valid choice.'


def test_valid_living_status():
    client = APIClient()
    url = "/npcs/"
    data = {
        "name": "Aria",
        "living_status": "Dead"
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["living_status"] == "Dead"


def test_invalid_relationship_to_party():
    client = APIClient()
    url = "/npcs/"
    data = {
        "name": "Aria",
        "relationship_to_party": "Invalid Option"
    }
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "relationship_to_party"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == '"Invalid Option" is not a valid choice.'


def test_valid_relationship_to_party():
    client = APIClient()
    url = "/npcs/"
    data = {
        "name": "Aria",
        "relationship_to_party": "Adversarial"
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["relationship_to_party"] == "Adversarial"
