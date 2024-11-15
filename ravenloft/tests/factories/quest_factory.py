import factory

from ravenloft.models import Quest


class QuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quest

    name = "Haunted Hotel"
    day_given = 2
    given_by = "Ruby (owner)"
    notes = "Shannon thinks it's ghosts. Guests disappeared from room 237."
    objective = "Find out what's been terrorizing hotel guests"
    reward = "200 gold"
    status = Quest.Status.IN_PROGRESS
