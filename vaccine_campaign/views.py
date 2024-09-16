from . import forms
from .models import VaccineCampaign, VaccineCampaignReview
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from vaccine_booking.models import VaccineBooking
from django.views.generic import FormView
from django.shortcuts import get_object_or_404


class CreateVaccineCampaign(LoginRequiredMixin, CreateView):
    model = VaccineCampaign
    form_class = forms.VaccineCampaignForm
    template_name = "create.html"
    success_url = reverse_lazy("campaign.index")
    login_url = "auth.login"

    def form_valid(self, form):
        messages.success(self.request, "Campaign Saved Successfully!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.account.type == "Doctor":
            return HttpResponse(
                "You do not have permission to view this page.", status=403
            )
        return super().dispatch(request, *args, **kwargs)


class UpdateVaccineCampaign(LoginRequiredMixin, UpdateView):
    model = VaccineCampaign
    form_class = forms.VaccineCampaignForm
    template_name = "create.html"
    login_url = "auth.login"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("campaign.index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Campaign Updated Successfully!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.account.type == "Doctor":
            return HttpResponse(
                "You do not have permission to view this page.", status=403
            )
        return super().dispatch(request, *args, **kwargs)


class VaccineCampaignList(LoginRequiredMixin, ListView):
    model = VaccineCampaign
    template_name = "list.html"
    context_object_name = "campaigns"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        campaign_ids = VaccineBooking.objects.filter(
            patient=self.request.user.account
        ).values_list("vaccine_campaign_id", flat=True)

        context["already_applied"] = list(campaign_ids)

        return context


class CampaignReviewView(FormView):
    template_name = "review.html"
    form_class = forms.CampaignReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["campaign"] = get_object_or_404(
            VaccineCampaign, pk=self.kwargs.get("pk")
        )
        if self.request.user.account.type == "Patient":
            context["reviews"] = VaccineCampaignReview.objects.filter(
                vaccine_campaign=context["campaign"], patient=self.request.user.account
            )
        else:
            context["reviews"] = VaccineCampaignReview.objects.filter(
                vaccine_campaign=context["campaign"]
            )
        return context

    def form_valid(self, form):
        campaign = get_object_or_404(VaccineCampaign, pk=self.kwargs.get("pk"))
        review = form.save(commit=False)
        review.vaccine_campaign = campaign
        review.patient = self.request.user.account
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("campaign.review", kwargs={"pk": self.kwargs.get("pk")})
