import pytest
from rest_framework.test import APIClient
from ravenloft.tests.factories.quest_factory import QuestFactory


@pytest.mark.django_db
def test_get_all_quests():
    QuestFactory.create_batch(size=2)
    client = APIClient()
    response = client.get("/quests/")

    assert response.status_code == 200
    assert len(response.data) == 2
