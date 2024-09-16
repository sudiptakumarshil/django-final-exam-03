from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from vaccine_campaign.models import VaccineCampaign
from .models import VaccineBooking
from .forms import VaccineBookingForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from core.decorators import doctor_required


@login_required(login_url=reverse_lazy("auth.login"))
@doctor_required
def apply_for_vaccine(request, campaign_id):
    campaign = get_object_or_404(VaccineCampaign, pk=campaign_id)

    if request.method == "POST":
        form = VaccineBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.patient = request.user.account
            booking.vaccine_campaign = campaign
            booking.save()
            messages.success(request, "You have successfully applied for the vaccine!")
            return redirect("campaign.index")
    else:
        form = VaccineBookingForm(initial={"campaign": campaign})

    return render(
        request, "apply_for_vaccine.html", {"form": form, "campaign": campaign}
    )


class VaccineBookingList(LoginRequiredMixin, ListView):
    model = VaccineBooking
    template_name = "booking_list.html"
    context_object_name = "booking"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
