from django.db import models
from vaccine_campaign.models import VaccineCampaign
from user.models import UserAccount


class VaccineBooking(models.Model):
    vaccine_campaign = models.ForeignKey(
        VaccineCampaign, related_name="vaccine_campaign", on_delete=models.CASCADE
    )
    patient = models.OneToOneField(
        UserAccount, related_name="patient", on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    is_completed = models.BooleanField()
