# Generated by Django 5.0.2 on 2024-02-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_delete_appointment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="date_of_birth",
        ),
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]