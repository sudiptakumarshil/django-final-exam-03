# Generated by Django 5.0.6 on 2024-09-17 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccineCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('location', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VaccineCampaignReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_reviews', to='user.useraccount')),
                ('vaccine_campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campaign_reviews', to='vaccine_campaign.vaccinecampaign')),
            ],
        ),
    ]
