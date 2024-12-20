# Generated by Django 5.1 on 2024-11-27 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravenloft', '0018_group_player_characters'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_member', models.BooleanField(default=True)),
                ('role', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ravenloft.group')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ravenloft.pet')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='pets',
            field=models.ManyToManyField(related_name='groups', through='ravenloft.GroupPet', to='ravenloft.pet'),
        ),
        migrations.AddConstraint(
            model_name='grouppet',
            constraint=models.UniqueConstraint(fields=('group', 'pet'), name='unique_group_pet'),
        ),
    ]
