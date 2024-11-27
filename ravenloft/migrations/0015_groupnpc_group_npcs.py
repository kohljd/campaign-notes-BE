# Generated by Django 5.1 on 2024-11-26 04:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravenloft', '0014_alter_group_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupNpc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_member', models.BooleanField(default=True)),
                ('role', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ravenloft.group')),
                ('npc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ravenloft.npc')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='npcs',
            field=models.ManyToManyField(related_name='groups', through='ravenloft.GroupNpc', to='ravenloft.npc'),
        ),
    ]
