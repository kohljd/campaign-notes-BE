from rest_framework import generics
from .models import Domain, Npc, Quest
from .serializers import DomainSerializer, NpcSerializer, QuestSerializer


class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class NpcList(generics.ListCreateAPIView):
    queryset = Npc.objects.all()
    serializer_class = NpcSerializer


class NpcDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Npc.objects.all()
    serializer_class = NpcSerializer


class QuestList(generics.ListCreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer


class QuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
