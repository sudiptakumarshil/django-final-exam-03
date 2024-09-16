from django.urls import path
from .views import apply_for_vaccine, VaccineBookingList

urlpatterns = [
    path(
        "campaign/<int:campaign_id>/apply/", apply_for_vaccine, name="apply_for_vaccine"
    ),
    path("index/", VaccineBookingList.as_view(), name="booking.index"),
]
