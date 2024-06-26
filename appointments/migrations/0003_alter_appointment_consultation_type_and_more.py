# Generated by Django 5.0.2 on 2024-02-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_consultation_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='consultation_type',
            field=models.CharField(choices=[('new_consultation', 'New Consultation'), ('prescription', 'Prescription Request'), ('follow_up', 'Follow-up Appointment')], default='new_consultation', max_length=30),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=20),
        ),
    ]
