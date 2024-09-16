from django import forms
from .models import VaccineCampaign
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import VaccineCampaignReview


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
        }

    def __init__(self, *args, **kwargs):
        super(VaccineCampaignForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))


class CampaignReviewForm(forms.ModelForm):
    comment = forms.Textarea()

    class Meta:
        model = VaccineCampaignReview
        fields = ["comment"]

    def __init__(self, *args, **kwargs):
        super(CampaignReviewForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
