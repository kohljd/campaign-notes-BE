import pytest

from django.db import IntegrityError
from ravenloft.models import Realm


@pytest.mark.django_db
def test_default_attributes():
    realm = Realm.objects.create(name="Lamordia")
    assert realm.name == "Lamordia"
    assert realm.domain_lord == "unknown"
    assert realm.notes == ""
    assert realm.updated_at is not None


@pytest.mark.django_db
def test_unique_name():
    Realm.objects.create(name="Lamordia")
    with pytest.raises(IntegrityError):
        Realm.objects.create(name="Lamordia")


@pytest.mark.django_db
def test_list_alphabetically_by_name():
    realm_1 = Realm.objects.create(name="Lamordia")
    realm_2 = Realm.objects.create(name="Barovia")
    assert list(Realm.objects.all()) == [realm_2, realm_1]


@pytest.mark.django_db
def test_list_by_name():
    realm = Realm.objects.create(name="Lamordia")
    assert str(realm) == "Lamordia"
