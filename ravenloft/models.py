from django.db import models


class CreatureSize(models.IntegerChoices):
    TINY = 1
    SMALL = 2
    MEDIUM = 3
    LARGE = 4
    HUGE = 5
    GARGANTUAN = 6


class LivingStatus(models.IntegerChoices):
    ALIVE = 1
    DEAD = 2
    UNKNOWN = 3


class PartyRelationship(models.IntegerChoices):
    FRIENDLY = 1
    NEUTRAL = 2
    ADVERSARIAL = 3
    UNCERTAIN = 4


class Creature(models.Model):
    name = models.CharField(unique=True, max_length=60)
    combat_notes = models.TextField(blank=True)
    description = models.TextField(blank=True)
    languages = models.TextField(default="None")
    notes = models.TextField(blank=True)
    size = models.IntegerField(
        choices=CreatureSize.choices,
        default=CreatureSize.MEDIUM
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(unique=True, max_length=60)
    domain_lord = models.CharField(default="unknown")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Group(models.Model):
    npcs = models.ManyToManyField("Npc", through="GroupNpc", related_name="groups")

    name = models.CharField(unique=True, max_length=60)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    relationship_to_party = models.IntegerField(
        choices=PartyRelationship.choices,
        default=PartyRelationship.NEUTRAL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class GroupNpc(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    npc = models.ForeignKey("Npc", on_delete=models.CASCADE)

    current_member = models.BooleanField(default=True)
    role = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["group", "npc"],
                name="unique_group_npc",
                violation_error_message="group npc association already exists"
            )
        ]


class Npc(models.Model):
    name = models.CharField(max_length=60)
    appearance = models.TextField(blank=True)
    living_status = models.IntegerField(
        choices=LivingStatus.choices,
        default=LivingStatus.ALIVE
    )
    relationship_to_party = models.IntegerField(
        choices=PartyRelationship.choices,
        default=PartyRelationship.NEUTRAL
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name", "pk"]

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(unique=True, max_length=60)
    description = models.TextField(blank=True)
    languages = models.TextField(default="None")
    living_status = models.IntegerField(
        choices=LivingStatus.choices,
        default=LivingStatus.ALIVE
    )
    notes = models.TextField(blank=True)
    size = models.IntegerField(
        choices=CreatureSize.choices,
        default=CreatureSize.MEDIUM
    )
    species = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlayerCharacter(models.Model):
    name = models.CharField(max_length=60)
    adventuring_goal = models.TextField(blank=True)
    appearance = models.TextField(blank=True)
    background = models.TextField(blank=True)
    deities = models.TextField(blank=True)
    dnd_class = models.CharField(max_length=30)
    living_status = models.IntegerField(
        choices=LivingStatus.choices,
        default=LivingStatus.ALIVE
    )
    notes = models.TextField(blank=True)
    race = models.CharField(max_length=30)
    size = models.IntegerField(
        choices=CreatureSize.choices,
        default=CreatureSize.MEDIUM
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Quest(models.Model):
    class Status(models.IntegerChoices):
        NOT_STARTED = 1
        IN_PROGRESS = 2
        PENDING_REWARD = 3
        COMPLETED = 4
        FAILED = 5
        PAUSED = 6
        ABANDONED = 7

    name = models.CharField(max_length=60)
    day_completed = models.PositiveIntegerField(null=True, blank=True)
    day_given = models.PositiveIntegerField()
    given_by = models.CharField(max_length=60)
    notes = models.TextField(blank=True)
    objective = models.TextField()
    reward = models.TextField(blank=True)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.NOT_STARTED
    )
    time_sensitive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(day_completed__isnull=True) |
                    models.Q(day_completed__gte=models.F("day_given"))
                ),
                name="if_provided_day_completed_must_be_gte_day_given",
                violation_error_message="day_completed cannot be before day_given"
            )
        ]

    def __str__(self):
        return self.name


class Session(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField()
    notes = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
