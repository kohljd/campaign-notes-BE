import pytest
from django.utils import dateparse
from rest_framework.test import APIClient
from ravenloft.tests.factories.quest_factory import QuestFactory


@pytest.mark.django_db
def test_get_quest():
    quest = QuestFactory()
    client = APIClient()
    response = client.get(f"/quests/{quest.id}/")
    created_at = dateparse.parse_datetime(response.data["created_at"])
    updated_at = dateparse.parse_datetime(response.data["updated_at"])

    assert response.status_code == 200
    assert response.data["id"] == quest.id
    assert response.data["name"] == quest.name
    assert created_at == quest.created_at
    assert response.data["day_completed"] == quest.day_completed
    assert response.data["day_given"] == quest.day_given
    assert response.data["notes"] == quest.notes
    assert response.data["objective"] == quest.objective
    assert response.data["reward"] == quest.reward
    assert response.data["status"] == quest.get_status_display()
    assert response.data["time_sensitive"] == quest.time_sensitive
    assert updated_at == quest.updated_at


@pytest.mark.django_db
def test_invalid_quest_id():
    client = APIClient()
    response = client.get("/quests/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Quest matches the given query."
