from django.contrib import admin
from .models import (Creature, Domain, Npc, Pet,
                     PlayerCharacter, Quest, Session)

admin.site.register(Creature)
admin.site.register(Domain)
admin.site.register(Npc)
admin.site.register(Pet)
admin.site.register(PlayerCharacter)
admin.site.register(Quest)
admin.site.register(Session)
