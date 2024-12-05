from rest_framework import serializers
from ravenloft.models import (Domain, LivingStatus, Npc, PartyRelationship, Quest)


class DisplayChoiceField(serializers.ChoiceField):
    def __init__(self, choices, **kwargs):
        super().__init__(choices=choices, **kwargs)

    def to_representation(self, value):
        return self.choices[value]

    def to_internal_value(self, data):
        reverse_choices = {v: k for k, v in self.choices.items()}
        if data in reverse_choices:
            return reverse_choices[data]
        return super().to_internal_value(data)


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = [
            "id",
            "name",
            "domain_lord",
            "notes",
            "created_at",
            "updated_at"
        ]


class NpcSerializer(serializers.ModelSerializer):
    living_status = DisplayChoiceField(choices=LivingStatus.choices, required=False)
    relationship_to_party = DisplayChoiceField(
        choices=PartyRelationship.choices,
        required=False
    )

    class Meta:
        model = Npc
        fields = [
            "id",
            "name",
            "appearance",
            "living_status",
            "relationship_to_party",
            "notes",
            "created_at",
            "updated_at"
        ]


class QuestSerializer(serializers.ModelSerializer):
    status = DisplayChoiceField(choices=Quest.Status.choices, required=False)

    class Meta:
        model = Quest
        fields = [
            "id",
            "name",
            "day_completed",
            "day_given",
            "given_by",
            "notes",
            "objective",
            "reward",
            "status",
            "time_sensitive",
            "created_at",
            "updated_at"
        ]

    def validate_day_completed(self, day_completed):
        data = self.initial_data
        quest = self.instance
        day_given = data.get("day_given")

        if day_given:
            day_given = int(day_given)
        elif quest:
            day_given = quest.day_given

        if day_completed and day_given and day_completed < day_given:
            raise serializers.ValidationError(
                "day_completed cannot be before day_given."
            )
        return day_completed

    def validate_day_given(self, day_given):
        data = self.initial_data
        quest = self.instance
        day_completed = data.get("day_completed")

        if day_completed:
            day_completed = int(day_given)
        elif quest:
            day_completed = quest.day_completed

        if day_completed and day_given and day_completed < day_given:
            raise serializers.ValidationError(
                "day_given cannot be after day_completed."
            )
        return day_given
