import pytest

from django.db import IntegrityError
from ravenloft.models import Group
from ..factories.group_factory import GroupFactory
from ..factories.npc_factory import NpcFactory
from ..factories.player_character_factory import PlayerCharacterFactory


@pytest.mark.django_db
def test_create_group_with_default_values():
    group = Group.objects.create(name="The Watchers")
    assert group.name == "The Watchers"
    assert group.description == ""
    assert group.notes == ""
    assert group.relationship_to_party == 2
    assert group.created_at is not None
    assert group.updated_at is not None
    assert group.get_relationship_to_party_display() == "Neutral"


@pytest.mark.django_db
def test_unique_name():
    GroupFactory(name="The Watchers")
    with pytest.raises(IntegrityError):
        GroupFactory(name="The Watchers")


@pytest.mark.django_db
def test_list_alphabetically_by_name():
    group_1 = GroupFactory(name="The Watchers")
    group_2 = GroupFactory(name="Another Name")
    assert list(Group.objects.all()) == [group_2, group_1]


@pytest.mark.django_db
def test_str():
    group = GroupFactory(name="The Watchers")
    assert str(group) == "The Watchers"


@pytest.mark.django_db
def test_group_has_many_npcs():
    npcs = NpcFactory.create_batch(size=2)
    group = GroupFactory(npcs=npcs)
    assert group.npcs.count() == 2


@pytest.mark.django_db
def test_group_has_many_pcs():
    pcs = PlayerCharacterFactory.create_batch(size=2)
    group = GroupFactory(player_characters=pcs)
    assert group.player_characters.count() == 2
