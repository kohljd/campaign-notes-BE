from rest_framework import serializers
from ravenloft.models import Realm


class RealmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realm
        fields = [
            "id",
            "name",
            "domain_lord",
            "notes",
            "updated_at"
        ]
