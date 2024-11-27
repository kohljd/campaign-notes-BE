import pytest

from django.db import IntegrityError
from ravenloft.models import GroupNpc
from ..factories.group_factory import GroupFactory
from ..factories.npc_factory import NpcFactory


@pytest.mark.django_db
def test_create_group_npc():
    group = GroupFactory(name="The Watchers")
    npc = NpcFactory(name="Aria")
    group_npc = GroupNpc.objects.create(
        group=group,
        npc=npc,
        current_member=False,
        role="Leader"
    )
    assert group_npc.group == group
    assert group_npc.npc == npc
    assert group_npc.current_member is False
    assert group_npc.role == "Leader"


@pytest.mark.django_db
def test_default_values():
    group_npc = GroupNpc.objects.create(group=GroupFactory(), npc=NpcFactory())
    assert group_npc.current_member is True
    assert group_npc.role == ""


@pytest.mark.django_db
def test_unique_group_npc():
    GroupNpc.objects.create(group=GroupFactory(), npc=NpcFactory())
    with pytest.raises(IntegrityError):
        GroupNpc.objects.create(group=GroupFactory(), npc=NpcFactory())


@pytest.mark.django_db
def test_deleting_group_deletes_associated_group_npcs():
    group_1 = GroupFactory(name="The Watchers")
    group_2 = GroupFactory(name="Another Name")
    npc_1 = NpcFactory()
    npc_2 = NpcFactory()
    npc_3 = NpcFactory()
    GroupNpc.objects.create(group=group_1, npc=npc_1)
    GroupNpc.objects.create(group=group_1, npc=npc_2)
    GroupNpc.objects.create(group=group_2, npc=npc_2)
    GroupNpc.objects.create(group=group_2, npc=npc_3)

    assert GroupNpc.objects.count() == 4
    assert group_1.npcs.count() == 2

    group_1.delete()
    assert GroupNpc.objects.count() == 2


@pytest.mark.django_db
def test_deleting_npc_deletes_associated_group_npcs():
    group_1 = GroupFactory(name="The Watchers")
    group_2 = GroupFactory(name="Another Name")
    npc_1 = NpcFactory()
    npc_2 = NpcFactory()
    npc_3 = NpcFactory()
    GroupNpc.objects.create(group=group_1, npc=npc_1)
    GroupNpc.objects.create(group=group_1, npc=npc_2)
    GroupNpc.objects.create(group=group_2, npc=npc_2)
    GroupNpc.objects.create(group=group_2, npc=npc_3)

    assert GroupNpc.objects.count() == 4
    assert npc_1.groups.count() == 1

    npc_1.delete()
    assert GroupNpc.objects.count() == 3
