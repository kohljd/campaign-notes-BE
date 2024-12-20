# Generated by Django 5.1 on 2024-11-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravenloft', '0009_alter_npc_options_alter_npc_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('adventuring_goal', models.TextField(blank=True)),
                ('appearance', models.TextField(blank=True)),
                ('background', models.TextField(blank=True)),
                ('dnd_class', models.CharField(max_length=30)),
                ('living_status', models.IntegerField(choices=[(1, 'Alive'), (2, 'Dead'), (3, 'Unknown')], default=1)),
                ('notes', models.TextField(blank=True)),
                ('race', models.CharField(max_length=30)),
                ('religion', models.CharField(blank=True, max_length=60)),
                ('size', models.IntegerField(choices=[(1, 'Tiny'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Huge'), (6, 'Gargantuan')], default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
