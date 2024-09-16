from django.db import models


# Create your models here.
class VaccineCampaign(models.Model):
    title = models.CharField(max_length=200, default="")
    location = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
