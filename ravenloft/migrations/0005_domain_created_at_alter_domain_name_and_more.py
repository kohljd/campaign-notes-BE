# Generated by Django 5.1 on 2024-11-13 22:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravenloft', '0004_quest_if_provided_day_completed_must_be_gte_day_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='objective',
            field=models.TextField(),
        ),
    ]
