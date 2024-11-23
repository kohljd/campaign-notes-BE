import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_quest():
    client = APIClient()
    url = "/quests/"
    data = {
        "name": "Haunted Hotel",
        "day_given": 2,
        "given_by": "Ruby (owner)",
        "notes": "Shannon thinks it's ghosts. Guests disappeared from room 237.",
        "objective": "Find out what's been terrorizing hotel guests",
        "reward": "200 gold"
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["id"] is not None
    assert response.data["name"] == data["name"]
    assert response.data["created_at"] is not None
    assert response.data["day_completed"] is None
    assert response.data["day_given"] == data["day_given"]
    assert response.data["notes"] == data["notes"]
    assert response.data["objective"] == data["objective"]
    assert response.data["reward"] == data["reward"]
    assert response.data["status"] == "Not Started"
    assert response.data["time_sensitive"] is False
    assert response.data["updated_at"] is not None


@pytest.mark.django_db
def test_default_values():
    client = APIClient()
    url = "/quests/"
    data = {
        "name": "Haunted Hotel",
        "day_given": 2,
        "given_by": "Ruby (owner)",
        "objective": "Find out what's been terrorizing hotel guests",
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["day_completed"] is None
    assert response.data["notes"] == ""
    assert response.data["objective"] == data["objective"]
    assert response.data["reward"] == ""
    assert response.data["status"] == "Not Started"
    assert response.data["time_sensitive"] is False


@pytest.mark.django_db
def test_invalid_day_completed():
    client = APIClient()
    url = "/quests/"
    data = {
        "name": "Haunted Hotel",
        "day_completed": 1,
        "day_given": 2,
        "given_by": "Ruby (owner)",
        "objective": "Find out what's been terrorizing hotel guests"
    }
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "day_completed"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == "day_completed cannot be before day_given."


@pytest.mark.django_db
def test_valid_day_completed():
    client = APIClient()
    url = "/quests/"
    data = {
        "name": "Haunted Hotel",
        "day_completed": 5,
        "day_given": 2,
        "given_by": "Ruby (owner)",
        "objective": "Find out what's been terrorizing hotel guests"
    }
    response = client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_invalid_status():
    client = APIClient()
    url = "/quests/"
    data = {
        "name": "Haunted Hotel",
        "day_given": 2,
        "given_by": "Ruby (owner)",
        "objective": "Find out what's been terrorizing hotel guests",
        "status": "Invalid Option"
    }
    response = client.post(url, data)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "status"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == '"Invalid Option" is not a valid choice.'


@pytest.mark.django_db
def test_valid_status():
    client = APIClient()
    url = "/quests/"
    data = {
        "name": "Haunted Hotel",
        "day_given": 2,
        "given_by": "Ruby (owner)",
        "objective": "Find out what's been terrorizing hotel guests",
        "status": "Paused"
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["status"] == "Paused"
