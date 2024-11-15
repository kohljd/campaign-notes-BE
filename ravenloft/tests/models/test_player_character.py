import pytest

from ravenloft.models import PlayerCharacter
from ..factories.player_character_factory import PlayerCharacterFactory


@pytest.mark.django_db
def test_create_pc_with_default_values():
    pc = PlayerCharacter.objects.create(
        name="Sophie",
        dnd_class="Sorcerer",
        race="Human"
    )
    assert pc.name == "Sophie"
    assert pc.adventuring_goal == ""
    assert pc.appearance == ""
    assert pc.background == ""
    assert pc.deities == ""
    assert pc.dnd_class == "Sorcerer"
    assert pc.living_status == 1
    assert pc.notes == ""
    assert pc.race == "Human"
    assert pc.size == 3
    assert pc.created_at is not None
    assert pc.updated_at is not None
    assert pc.get_living_status_display() == "Alive"
    assert pc.get_size_display() == "Medium"


@pytest.mark.django_db
def test_list_alphabetically_by_name():
    pc_1 = PlayerCharacterFactory(name="Sophie")
    pc_2 = PlayerCharacterFactory(name="Howl")
    pc_3 = PlayerCharacterFactory(name="Calcifer")
    assert list(PlayerCharacter.objects.all()) == [pc_3, pc_2, pc_1]


@pytest.mark.django_db
def test_str():
    pc = PlayerCharacterFactory(name="Sophie")
    assert str(pc) == "Sophie"
