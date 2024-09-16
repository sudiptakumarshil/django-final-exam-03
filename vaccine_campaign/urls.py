from django.urls import path
from .views import (
    CreateVaccineCampaign,
    UpdateVaccineCampaign,
    VaccineCampaignList,
    CampaignReviewView,
)

urlpatterns = [
    path("create/", CreateVaccineCampaign.as_view(), name="campaign.create"),
    path("edit/<int:id>/", UpdateVaccineCampaign.as_view(), name="campaign.edit"),
    path("index/", VaccineCampaignList.as_view(), name="campaign.index"),
    path("review/<int:pk>/", CampaignReviewView.as_view(), name="campaign.review")
]
