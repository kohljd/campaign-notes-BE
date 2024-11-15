import factory

from ravenloft.models import CreatureSize, Creature


class CreatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Creature

    name = "Dragon Turtle"
    combat_notes = "fire resistance, can breath underwater"
    description = "Massive snapping turtle with a dragon head"
    languages = "Aquan, Draconic"
    notes = "Encountered one on the Forbidden Sea"
    size = CreatureSize.GARGANTUAN
