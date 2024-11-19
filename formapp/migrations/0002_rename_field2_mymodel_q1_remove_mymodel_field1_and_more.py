# Generated by Django 5.0.4 on 2024-04-12 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mymodel",
            old_name="field2",
            new_name="q1",
        ),
        migrations.RemoveField(
            model_name="mymodel",
            name="field1",
        ),
        migrations.AddField(
            model_name="mymodel",
            name="q2",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
