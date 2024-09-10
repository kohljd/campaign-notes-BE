from rest_framework import generics
from .models import Realm
from .serializers import RealmSerializer


class RealmList(generics.ListCreateAPIView):
    queryset = Realm.objects.all()
    serializer_class = RealmSerializer


class RealmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Realm.objects.all()
    serializer_class = RealmSerializer
