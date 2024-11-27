import pytest

from django.db import IntegrityError
from ravenloft.models import Pet
from ..factories.group_factory import GroupFactory
from ..factories.pet_factory import PetFactory


@pytest.mark.django_db
def test_create_pet_with_default_values():
    pet = Pet.objects.create(
        name="Bambi",
        species="Deer"
    )
    assert pet.name == "Bambi"
    assert pet.description == ""
    assert pet.languages == "None"
    assert pet.living_status == 1
    assert pet.notes == ""
    assert pet.size == 3
    assert pet.species == "Deer"
    assert pet.created_at is not None
    assert pet.updated_at is not None
    assert pet.get_living_status_display() == "Alive"
    assert pet.get_size_display() == "Medium"


@pytest.mark.django_db
def test_unique_name():
    PetFactory(name="Samson")
    with pytest.raises(IntegrityError):
        PetFactory(name="Samson")


@pytest.mark.django_db
def test_list_alphabetically_by_name():
    pet_1 = PetFactory(name="Samson")
    pet_2 = PetFactory(name="Lassie")
    pet_3 = PetFactory(name="Bambi")
    assert list(Pet.objects.all()) == [pet_3, pet_2, pet_1]


@pytest.mark.django_db
def test_str():
    pet = PetFactory(name="Samson")
    assert str(pet) == "Samson"


@pytest.mark.django_db
def test_can_be_a_member_of_multiple_groups():
    group_1 = GroupFactory(name="Group1")
    group_2 = GroupFactory(name="Group2")
    pet = PetFactory()
    pet.groups.add(group_1, group_2)
    assert pet.groups.count() == 2
