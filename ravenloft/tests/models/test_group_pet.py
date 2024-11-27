import pytest

from django.db import IntegrityError
from ravenloft.models import GroupPet
from ..factories.group_factory import GroupFactory
from ..factories.pet_factory import PetFactory


@pytest.mark.django_db
def test_create_group_pet():
    group = GroupFactory()
    pet = PetFactory()
    group_pet = GroupPet.objects.create(
        group=group,
        pet=pet,
        current_member=False,
        role="Mascot"
    )
    assert group_pet.group == group
    assert group_pet.pet == pet
    assert group_pet.current_member is False
    assert group_pet.role == "Mascot"


@pytest.mark.django_db
def test_default_values():
    group_pet = GroupPet.objects.create(
        group=GroupFactory(),
        pet=PetFactory(),
    )
    assert group_pet.current_member is True
    assert group_pet.role == ""


@pytest.mark.django_db
def test_unique_group_pet():
    group = GroupFactory()
    pet = PetFactory()
    GroupPet.objects.create(
        group=group,
        pet=pet,
    )
    with pytest.raises(IntegrityError):
        GroupPet.objects.create(
            group=group,
            pet=pet,
        )


@pytest.mark.django_db
def test_deleting_group_deletes_associated_group_pets():
    group_1 = GroupFactory(name="The Watchers")
    group_2 = GroupFactory(name="Another Name")
    pet_1 = PetFactory(name="Samson")
    pet_2 = PetFactory(name="Lassie")
    pet_3 = PetFactory(name="Bambi")
    GroupPet.objects.create(group=group_1, pet=pet_1)
    GroupPet.objects.create(group=group_1, pet=pet_2)
    GroupPet.objects.create(group=group_2, pet=pet_2)
    GroupPet.objects.create(group=group_2, pet=pet_3)

    assert GroupPet.objects.count() == 4
    assert group_1.pets.count() == 2

    group_1.delete()
    assert GroupPet.objects.count() == 2


@pytest.mark.django_db
def test_deleting_pet_deletes_associated_group_pets():
    group_1 = GroupFactory(name="The Watchers")
    group_2 = GroupFactory(name="Another Name")
    pet_1 = PetFactory(name="Samson")
    pet_2 = PetFactory(name="Lassie")
    pet_3 = PetFactory(name="Bambi")
    GroupPet.objects.create(group=group_1, pet=pet_1)
    GroupPet.objects.create(group=group_1, pet=pet_2)
    GroupPet.objects.create(group=group_2, pet=pet_2)
    GroupPet.objects.create(group=group_2, pet=pet_3)

    assert GroupPet.objects.count() == 4
    assert pet_1.groups.count() == 1

    pet_1.delete()
    assert GroupPet.objects.count() == 3
