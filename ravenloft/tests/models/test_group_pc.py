import pytest

from django.db import IntegrityError
from ravenloft.models import GroupPlayerCharacter
from ..factories.group_factory import GroupFactory
from ..factories.player_character_factory import PlayerCharacterFactory


@pytest.mark.django_db
def test_create_group_pc():
    group = GroupFactory()
    pc = PlayerCharacterFactory()
    group_pc = GroupPlayerCharacter.objects.create(
        group=group,
        player_character=pc,
        current_member=False,
        role="Leader"
    )
    assert group_pc.group == group
    assert group_pc.player_character == pc
    assert group_pc.current_member is False
    assert group_pc.role == "Leader"


@pytest.mark.django_db
def test_default_values():
    group_pc = GroupPlayerCharacter.objects.create(
        group=GroupFactory(),
        player_character=PlayerCharacterFactory(),
    )
    assert group_pc.current_member is True
    assert group_pc.role == ""


@pytest.mark.django_db
def test_unique_group_pc():
    group = GroupFactory()
    pc = PlayerCharacterFactory()
    GroupPlayerCharacter.objects.create(
        group=group,
        player_character=pc,
    )
    with pytest.raises(IntegrityError):
        GroupPlayerCharacter.objects.create(
            group=group,
            player_character=pc,
        )
