import pytest
from django.utils import dateparse
from rest_framework.test import APIClient
from ravenloft.tests.factories.quest_factory import QuestFactory


@pytest.mark.django_db
def test_update_quest():
    quest = QuestFactory(name="Haunted Hotel", notes="")
    client = APIClient()
    body = {
        "name": "Ghost Hunt",
        "notes": "Lots of ghosts"
    }
    original_updated_at = quest.updated_at
    response = client.patch(f"/quests/{quest.id}/", body)
    updated_at = dateparse.parse_datetime(response.data["updated_at"])

    assert response.status_code == 200
    assert response.data["name"] == "Ghost Hunt"
    assert response.data["notes"] == "Lots of ghosts"
    assert updated_at > original_updated_at


@pytest.mark.django_db
def test_invalid_status():
    quest = QuestFactory()
    client = APIClient()
    body = {"status": "Scooby-Doo"}
    response = client.patch(f"/quests/{quest.id}/", body)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "status"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == '"Scooby-Doo" is not a valid choice.'


@pytest.mark.django_db
def test_valid_status():
    quest = QuestFactory()
    client = APIClient()
    body = {"status": "Paused"}
    response = client.patch(f"/quests/{quest.id}/", body)

    assert response.status_code == 200
    assert response.data["status"] == "Paused"


@pytest.mark.django_db
def test_invalid_quest_id():
    client = APIClient()
    response = client.patch("/quests/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Quest matches the given query."


@pytest.mark.django_db
def test_invalid_day_completed():
    quest = QuestFactory(day_given=5, day_completed=7)
    client = APIClient()
    body = {"day_completed": 3}
    response = client.patch(f"/quests/{quest.id}/", body)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "day_completed"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == "day_completed cannot be before day_given."


@pytest.mark.django_db
def test_invalid_day_given():
    quest = QuestFactory(day_given=5, day_completed=7)
    client = APIClient()
    body = {"day_given": 10}
    response = client.patch(f"/quests/{quest.id}/", body)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "day_given"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == "day_given cannot be after day_completed."
