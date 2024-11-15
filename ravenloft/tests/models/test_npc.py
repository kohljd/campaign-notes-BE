import pytest

from ravenloft.models import Npc
from ..factories.npc_factory import NpcFactory


@pytest.mark.django_db
def test_create_npc_with_default_values():
    npc = Npc.objects.create(name="Aria")
    assert npc.name == "Aria"
    assert npc.appearance == ""
    assert npc.living_status == 1
    assert npc.relationship_to_party == 2
    assert npc.notes == ""
    assert npc.created_at is not None
    assert npc.updated_at is not None
    assert npc.get_living_status_display() == "Alive"
    assert npc.get_relationship_to_party_display() == "Neutral"


@pytest.mark.django_db
def test_list_alphabetically_by_name_then_pk():
    npc_1 = NpcFactory(name="Aria")
    npc_2 = NpcFactory(name="Leo")
    npc_3 = NpcFactory(name="Aria")
    assert list(Npc.objects.all()) == [npc_1, npc_3, npc_2]


@pytest.mark.django_db
def test_str():
    npc = NpcFactory(name="Aria")
    assert str(npc) == "Aria"
