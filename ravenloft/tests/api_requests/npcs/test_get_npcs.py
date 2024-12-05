import pytest
from rest_framework.test import APIClient
from ravenloft.tests.factories.npc_factory import NpcFactory


@pytest.mark.django_db
def test_get_all_npcs():
    NpcFactory.create_batch(size=2)
    client = APIClient()
    response = client.get("/npcs/")

    assert response.status_code == 200
    assert len(response.data) == 2
