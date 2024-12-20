import pytest

from django.core.exceptions import ValidationError
from ravenloft.models import Session
from ..factories.session_factory import SessionFactory


@pytest.mark.django_db
def test_create_session_with_default_values():
    session = Session.objects.create(
        title="Dinner Party with Ghosts",
        date="2024-10-31"
    )
    assert session.title == "Dinner Party with Ghosts"
    assert session.date == "2024-10-31"
    assert session.notes == ""
    assert session.summary == ""
    assert session.created_at is not None
    assert session.updated_at is not None


@pytest.mark.django_db
def test_invalid_date_format():
    with pytest.raises(ValidationError):
        SessionFactory(date="10/31/2024")
    with pytest.raises(ValidationError):
        SessionFactory(date="2024, 10, 31")
    with pytest.raises(ValidationError):
        SessionFactory(date="October 13, 2024")


@pytest.mark.django_db
def test_list_sessions_by_newest_to_oldest_date():
    session_1 = SessionFactory(date="2023-11-16")
    session_2 = SessionFactory(date="2024-10-31")
    session_3 = SessionFactory(date="2024-11-16")
    assert list(Session.objects.all()) == [session_3, session_2, session_1]


@pytest.mark.django_db
def test_str():
    session = SessionFactory(title="Dinner Party with Ghosts")
    assert str(session) == "Dinner Party with Ghosts"
