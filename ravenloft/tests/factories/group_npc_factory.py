import factory

from ravenloft.models import GroupNpc
from .group_factory import GroupFactory
from .npc_factory import NpcFactory


class GroupNpcFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupNpc

    group = factory.SubFactory(GroupFactory)
    npc = factory.SubFactory(NpcFactory)
