import factory

from ravenloft.models import Group, PartyRelationship


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = "The Watchers"
    description = "The keepers of Ravenloft"
    notes = "Can travel to any domain"
    relationship_to_party = PartyRelationship.FRIENDLY
