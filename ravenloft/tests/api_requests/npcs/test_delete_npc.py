import pytest
from rest_framework.test import APIClient
from ravenloft.tests.factories.npc_factory import NpcFactory
pytestmark = pytest.mark.django_db


def test_delete_npc():
    npc = NpcFactory()
    client = APIClient()
    response = client.delete(f"/npcs/{npc.id}/")

    assert response.status_code == 204


def test_invalid_npc_id():
    client = APIClient()
    response = client.get("/npcs/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Npc matches the given query."
