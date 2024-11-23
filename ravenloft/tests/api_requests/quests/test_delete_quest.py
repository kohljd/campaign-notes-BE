import pytest
from rest_framework.test import APIClient
from ravenloft.tests.factories.quest_factory import QuestFactory


@pytest.mark.django_db
def test_delete_quest():
    quest = QuestFactory()
    client = APIClient()
    response = client.delete(f"/quests/{quest.id}/")

    assert response.status_code == 204


@pytest.mark.django_db
def test_invalid_quest_id():
    client = APIClient()
    response = client.delete("/quests/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Quest matches the given query."
