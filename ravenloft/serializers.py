from rest_framework import serializers
from ravenloft.models import Domain


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
