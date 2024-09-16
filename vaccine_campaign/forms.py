from django import forms
from .models import VaccineCampaign
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class VaccineCampaignForm(forms.ModelForm):
    class Meta:
        model = VaccineCampaign
        fields = "__all__"
        widgets = {
            "start_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                    "placeholder": "Select start date and time",
                }
            ),
            "end_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                    "placeholder": "Select end date and time",
                }
            ),
            "category": forms.SelectMultiple(attrs={"class": "select2 form-control"}),
            "author": forms.Select(attrs={"class": "select2 form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(VaccineCampaignForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
