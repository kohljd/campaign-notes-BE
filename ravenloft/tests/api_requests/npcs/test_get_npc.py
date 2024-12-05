import pytest
from django.utils import dateparse
from rest_framework.test import APIClient
from ravenloft.tests.factories.npc_factory import NpcFactory
pytestmark = pytest.mark.django_db


def test_get_npc():
    npc = NpcFactory()
    client = APIClient()
    response = client.get(f"/npcs/{npc.id}/")

    created_at = dateparse.parse_datetime(response.data["created_at"])
    updated_at = dateparse.parse_datetime(response.data["updated_at"])
    relationship_to_party = response.data["relationship_to_party"]

    assert response.status_code == 200
    assert response.data["id"] == npc.id
    assert response.data["name"] == npc.name
    assert response.data["appearance"] == npc.appearance
    assert response.data["living_status"] == npc.get_living_status_display()
    assert relationship_to_party == npc.get_relationship_to_party_display()
    assert response.data["notes"] == npc.notes
    assert created_at == npc.created_at
    assert updated_at == npc.updated_at


def test_invalid_npc_id():
    client = APIClient()
    response = client.get("/npcs/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Npc matches the given query."
