import factory

from ravenloft.models import Domain


class DomainFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Domain

    name = "Lamordia"
    domain_lord = "Dr. Viktra Mordenhein"
    notes = "It's cold, smoggy, and the forest has radiation"
