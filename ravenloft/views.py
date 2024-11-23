from rest_framework import generics
from .models import Domain, Quest
from .serializers import DomainSerializer, QuestSerializer


class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class QuestList(generics.ListCreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer


class QuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
