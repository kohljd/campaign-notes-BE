import pytest

from django.db import IntegrityError
from ravenloft.models import Domain


@pytest.mark.django_db
def test_default_attributes():
    domain = Domain.objects.create(name="Lamordia")
    assert domain.name == "Lamordia"
    assert domain.domain_lord == "unknown"
    assert domain.notes == ""
    assert domain.updated_at is not None


@pytest.mark.django_db
def test_unique_name():
    Domain.objects.create(name="Lamordia")
    with pytest.raises(IntegrityError):
        Domain.objects.create(name="Lamordia")


@pytest.mark.django_db
def test_list_alphabetically_by_name():
    domain_1 = Domain.objects.create(name="Lamordia")
    domain_2 = Domain.objects.create(name="Barovia")
    assert list(Domain.objects.all()) == [domain_2, domain_1]


@pytest.mark.django_db
def test_list_by_name():
    domain = Domain.objects.create(name="Lamordia")
    assert str(domain) == "Lamordia"
