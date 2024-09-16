from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from user.models import UserAccount
from vaccine_campaign.models import VaccineCampaign

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy("auth.login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_doctor"] = UserAccount.objects.filter(type="Doctor").count()
        context["total_patient"] = UserAccount.objects.filter(type="Patient").count()
        context['total_campaign'] = VaccineCampaign.objects.count()
        return context
