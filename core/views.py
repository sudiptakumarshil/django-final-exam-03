from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy("auth.login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["categories"] = Category.objects.filter(status=True).values(
        #     "id", "name", "slug"
        # )
        # context["books"] = Book.objects.filter(status=True)[:5]
        return context
