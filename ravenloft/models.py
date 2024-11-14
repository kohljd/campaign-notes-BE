from django.db import models


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
