import factory

from ravenloft.models import CreatureSize, Pet


class PetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pet

    name = "Samson"
    description = "orange striped cat"
    notes = "will do anything for catnip"
    size = CreatureSize.TINY
    species = "Cat"
