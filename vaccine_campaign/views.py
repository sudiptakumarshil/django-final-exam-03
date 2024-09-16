from . import forms
from .models import VaccineCampaign
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.account.type == "Doctor":
            return HttpResponse(
                "You do not have permission to view this page.", status=403
            )
        return super().dispatch(request, *args, **kwargs)
