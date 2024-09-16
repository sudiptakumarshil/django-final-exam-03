from django.views.generic import FormView, TemplateView
from .forms import UserRegistrationForm, UserUpdateForm, CustomPasswordChangeForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.db import transaction, DatabaseError
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect


class UserRegistrationView(FormView):
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("auth.login")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("home"))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = form.save()
                login(self.request, user)
                return super().form_valid(form)
        except DatabaseError as e:
            form.add_error(None, "An error occured")
            return self.form_invalid(form)


class UserLoginView(LoginView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("home"))
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy("home")


class UserUpdateView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserUpdateForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated!")
            return redirect("profile")
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return redirect(reverse_lazy("home"))


class UserPasswordChangeView(PasswordChangeView):
    template_name = "password_change_form.html"
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "Your password has been changed successfully!")
        return super().form_valid(form)
