import pytest
from django.utils import dateparse
from rest_framework.test import APIClient
from ravenloft.tests.factories.npc_factory import NpcFactory
pytestmark = pytest.mark.django_db


def test_update_npc():
    npc = NpcFactory(
        living_status=1,            # Alive
        relationship_to_party=2     # Neutral
    )
    client = APIClient()
    body = {
        "name": "Updated Name",
        "appearance": "Updated Appearance",
        "living_status": "Unknown",
        "relationship_to_party": "Uncertain",
        "notes": "Updated Notes"
    }
    response = client.patch(f"/npcs/{npc.id}/", body)

    original_updated_at = npc.updated_at
    updated_at = dateparse.parse_datetime(response.data["updated_at"])

    assert response.status_code == 200
    assert response.data["id"] == npc.id
    assert response.data["name"] == "Updated Name"
    assert response.data["appearance"] == "Updated Appearance"
    assert response.data["living_status"] == "Unknown"
    assert response.data["relationship_to_party"] == "Uncertain"
    assert response.data["notes"] == "Updated Notes"
    assert updated_at > original_updated_at


def test_invalid_npc_id():
    client = APIClient()
    response = client.patch("/npcs/0/")

    assert response.status_code == 404
    assert response.data["title"] == "Not Found"

    error = response.data["errors"][0]
    assert error["detail"] == "No Npc matches the given query."


def test_invalid_name_length():
    npc = NpcFactory(name="Aria")
    client = APIClient()
    body = {"name": "A" * 61}
    response = client.patch(f"/npcs/{npc.id}/", body)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "name"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == "Ensure this field has no more than 60 characters."


def test_invalid_living_status():
    npc = NpcFactory()
    client = APIClient()
    body = {"living_status": "Invalid Status"}
    response = client.patch(f"/npcs/{npc.id}/", body)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "living_status"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == '"Invalid Status" is not a valid choice.'


def test_invalid_relationship_to_party():
    npc = NpcFactory()
    client = APIClient()
    body = {"relationship_to_party": "Invalid Option"}
    response = client.patch(f"/npcs/{npc.id}/", body)

    assert response.status_code == 400
    assert response.data["title"] == "Validation Error"

    error = response.data["errors"][0]
    assert error["field"] == "relationship_to_party"

    error_detail = error["field_errors"][0]["detail"]
    assert error_detail == '"Invalid Option" is not a valid choice.'
