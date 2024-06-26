# Generated by Django 5.0.2 on 2024-03-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prescriptions", "0002_prescription_appointment_alter_prescription_doctor"),
    ]

    operations = [
        migrations.AddField(
            model_name="prescription",
            name="prescription_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="prescription_images/"
            ),
        ),
    ]
