import factory

from ravenloft.models import Group, PartyRelationship


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = "The Watchers"
    description = "The keepers of Ravenloft"
    notes = "Can travel to any domain"
    relationship_to_party = PartyRelationship.FRIENDLY

    @factory.post_generation
    def npcs(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.npcs.add(*extracted)

    @factory.post_generation
    def player_characters(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.player_characters.add(*extracted)
