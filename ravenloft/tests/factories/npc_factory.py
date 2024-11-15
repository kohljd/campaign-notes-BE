import factory

from ravenloft.models import Npc


class NpcFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Npc

    name = "Aria"
    appearance = "Mid-30's half-elf woman in commoner clothes"
    notes = "Lives in Ludendorf. Works at the theater."
