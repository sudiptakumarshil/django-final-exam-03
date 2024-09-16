from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE, USER_TYPE


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    nid = models.CharField(unique=True, max_length=50, null=True)
    type = models.CharField(max_length=20, choices=USER_TYPE, default="Patient")

    def __str__(self):
        return str(self.user.first_name)
