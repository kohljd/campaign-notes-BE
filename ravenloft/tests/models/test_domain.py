import pytest

from django.db import IntegrityError
from ravenloft.models import Domain
from ..factories.domain_factory import DomainFactory


@pytest.mark.django_db
def test_default_attributes():
    domain = Domain.objects.create(name="Lamordia")
    assert domain.name == "Lamordia"
    assert domain.domain_lord == "unknown"
    assert domain.notes == ""
    assert domain.created_at is not None
    assert domain.updated_at is not None


@pytest.mark.django_db
def test_unique_name():
    DomainFactory(name="Lamordia")
    with pytest.raises(IntegrityError):
        DomainFactory(name="Lamordia")


@pytest.mark.django_db
def test_list_alphabetically_by_name():
    domain_1 = DomainFactory(name="Lamordia")
    domain_2 = DomainFactory(name="Barovia")
    assert list(Domain.objects.all()) == [domain_2, domain_1]


@pytest.mark.django_db
def test_str():
    domain = DomainFactory(name="Lamordia")
    assert str(domain) == "Lamordia"
