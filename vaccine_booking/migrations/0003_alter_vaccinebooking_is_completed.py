# Generated by Django 5.0.6 on 2024-09-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_booking', '0002_vaccinebooking_delete_vaccinecampaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinebooking',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
