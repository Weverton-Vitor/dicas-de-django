# Generated by Django 2.2.13 on 2020-06-14 08:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.UUIDField(default=uuid.UUID('4194db20-ff52-4852-a426-516080e18490'), editable=False, unique=True),
        ),
    ]
