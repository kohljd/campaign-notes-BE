from django.db import models


class Realm(models.Model):
    name = models.CharField(unique=True)
    domain_lord = models.CharField(default="unknown")
    notes = models.TextField(blank=True, default="")
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
