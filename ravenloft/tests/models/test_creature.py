import pytest

from django.db import IntegrityError
from ravenloft.models import Creature
from ..factories.creature_factory import CreatureFactory


@pytest.mark.django_db
def test_create_creature_with_default_values():
    creature = Creature.objects.create(name="Dragon Turtle")
    assert creature.name == "Dragon Turtle"
    assert creature.combat_notes == ""
    assert creature.description == ""
    assert creature.languages == "None"
    assert creature.notes == ""
    assert creature.size == 3
    assert creature.created_at is not None
    assert creature.updated_at is not None
    assert creature.get_size_display() == "Medium"


@pytest.mark.django_db
def test_unique_name():
    CreatureFactory(name="Dragon Turtle")
    with pytest.raises(IntegrityError):
        CreatureFactory(name="Dragon Turtle")


@pytest.mark.django_db
def test_list_alphabetically_by_name():
    creature_1 = CreatureFactory(name="Zombie")
    creature_2 = CreatureFactory(name="Owlbear")
    creature_3 = CreatureFactory(name="Beholder")
    assert list(Creature.objects.all()) == [creature_3, creature_2, creature_1]


@pytest.mark.django_db
def test_str():
    creature = CreatureFactory(name="Dragon Turtle")
    assert str(creature) == "Dragon Turtle"
