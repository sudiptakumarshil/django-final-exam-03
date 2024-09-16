from django.db import models
from user.models import UserAccount


# Create your models here.
class VaccineCampaign(models.Model):
    title = models.CharField(max_length=200, default="")
    location = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title


class VaccineCampaignReview(models.Model):
    comment = models.TextField()
    vaccine_campaign = models.ForeignKey(
        VaccineCampaign, related_name="campaign_reviews", on_delete=models.CASCADE
    )
    patient = models.ForeignKey(
        UserAccount, related_name="patient_reviews", on_delete=models.CASCADE
    )
    def __str__(self):
        return f"Review by {self.patient} for {self.vaccine_campaign}"
