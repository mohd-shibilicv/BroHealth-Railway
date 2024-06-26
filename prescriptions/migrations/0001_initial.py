# Generated by Django 5.0.2 on 2024-03-12 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("doctors", "0006_remove_doctor_consultation_fee"),
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("medication_details", models.TextField()),
                ("dosage", models.CharField(max_length=255)),
                ("additional_instructions", models.TextField(blank=True, null=True)),
                ("prescription_date", models.DateField(auto_now=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prescriptions",
                        to="doctors.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prescriptions",
                        to="patients.patient",
                    ),
                ),
            ],
        ),
    ]
