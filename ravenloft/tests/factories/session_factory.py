import factory

from ravenloft.models import Session


class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Session

    title = "Dinner Party with Ghosts"
    date = "2024-10-31"
    notes = "Like that scene from Casper, but no actual food"
    summary = "Ghost food = still hungry"
