import pytest

from django.db import IntegrityError
from ravenloft.models import Quest
from ..factories.quest_factory import QuestFactory


@pytest.mark.django_db
def test_create_quest_with_default_values():
    quest = Quest.objects.create(
        name="Haunted Hotel",
        day_given=2,
        given_by="Ruby (owner)",
        objective="Find out what's been terrorizing hotel guests"
    )
    assert quest.name == "Haunted Hotel"
    assert quest.day_completed is None
    assert quest.day_given == 2
    assert quest.given_by == "Ruby (owner)"
    assert quest.notes == ""
    assert quest.objective == "Find out what's been terrorizing hotel guests"
    assert quest.reward == ""
    assert quest.status == 1
    assert quest.time_sensitive is False
    assert quest.created_at is not None
    assert quest.updated_at is not None


@pytest.mark.django_db
def test_day_completed_cannot_be_before_day_given():
    with pytest.raises(IntegrityError):
        QuestFactory(
            day_completed=1,
            day_given=2
        )


@pytest.mark.django_db
def test_day_completed_on_day_given():
    quest = QuestFactory(
        day_completed=2,
        day_given=2
    )
    assert quest.day_completed == 2
    assert quest.day_given == 2


@pytest.mark.django_db
def test_day_completed_after_day_given():
    quest = QuestFactory(
        day_completed=5,
        day_given=2,
    )
    assert quest.day_completed == 5
    assert quest.day_given == 2


@pytest.mark.django_db
def test_str():
    quest = QuestFactory(name="Haunted Hotel")
    assert str(quest) == "Haunted Hotel"
