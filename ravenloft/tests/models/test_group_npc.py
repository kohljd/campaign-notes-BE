import pytest

from django.db import IntegrityError
from ravenloft.models import Group, GroupNpc, Npc
from ..factories.group_npc_factory import GroupNpcFactory


@pytest.mark.django_db
def test_create_group_npc():
    group = Group.objects.create(name="The Watchers")
    npc = Npc.objects.create(name="Aria")
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
    group_npc = GroupNpcFactory()
    assert group_npc.current_member is True
    assert group_npc.role == ""


@pytest.mark.django_db
def test_unique_group_npc():
    GroupNpcFactory()
    with pytest.raises(IntegrityError):
        GroupNpcFactory()
