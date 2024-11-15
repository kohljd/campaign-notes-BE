import factory

from ravenloft.models import PlayerCharacter


class PlayerCharacterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlayerCharacter

    name = "Sophie"
    adventuring_goal = "reverse my curse"
    appearance = "Gray haired old lady in a blue dress with a red shawl and cane"
    background = "Used to make hats in a small shop before adventuring"
    dnd_class = "Sorcerer"
    notes = "Random scarecrow and dog follows her around"
    race = "Human"
