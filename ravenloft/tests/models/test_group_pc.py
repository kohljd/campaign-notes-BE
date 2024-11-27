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


@pytest.mark.django_db
def test_deleting_group_deletes_associated_group_pcs():
    group_1 = GroupFactory(name="The Watchers")
    group_2 = GroupFactory(name="Another Name")
    pc_1 = PlayerCharacterFactory()
    pc_2 = PlayerCharacterFactory()
    pc_3 = PlayerCharacterFactory()
    GroupPlayerCharacter.objects.create(group=group_1, player_character=pc_1)
    GroupPlayerCharacter.objects.create(group=group_1, player_character=pc_2)
    GroupPlayerCharacter.objects.create(group=group_2, player_character=pc_2)
    GroupPlayerCharacter.objects.create(group=group_2, player_character=pc_3)

    assert GroupPlayerCharacter.objects.count() == 4
    assert group_1.player_characters.count() == 2

    group_1.delete()
    assert GroupPlayerCharacter.objects.count() == 2


@pytest.mark.django_db
def test_deleting_pc_deletes_associated_group_pcs():
    group_1 = GroupFactory(name="The Watchers")
    group_2 = GroupFactory(name="Another Name")
    pc_1 = PlayerCharacterFactory()
    pc_2 = PlayerCharacterFactory()
    pc_3 = PlayerCharacterFactory()
    GroupPlayerCharacter.objects.create(group=group_1, player_character=pc_1)
    GroupPlayerCharacter.objects.create(group=group_1, player_character=pc_2)
    GroupPlayerCharacter.objects.create(group=group_2, player_character=pc_2)
    GroupPlayerCharacter.objects.create(group=group_2, player_character=pc_3)

    assert GroupPlayerCharacter.objects.count() == 4
    assert pc_1.groups.count() == 1

    pc_1.delete()
    assert GroupPlayerCharacter.objects.count() == 3
