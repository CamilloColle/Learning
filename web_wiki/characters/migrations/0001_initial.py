# Generated by Django 5.1.7 on 2025-03-17 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=50)),
                ('alignment', models.CharField(max_length=50)),
                ('backstory', models.TextField(blank=True)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='campaigns.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='NonPlayerCharacter',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='characters.character')),
                ('role', models.CharField(choices=[('ALLY', 'Ally'), ('ENEMY', 'Enemy'), ('NEUTRAL', 'Neutral'), ('OTHER', 'Other')], default='NEUTRAL', max_length=50)),
            ],
            bases=('characters.character',),
        ),
        migrations.CreateModel(
            name='PlayerCharacter',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='characters.character')),
                ('character_class', models.CharField(max_length=50)),
                ('player_name', models.CharField(max_length=100)),
                ('character_sheet', models.FileField(blank=True, null=True, upload_to='character_sheets/')),
            ],
            bases=('characters.character',),
        ),
    ]
