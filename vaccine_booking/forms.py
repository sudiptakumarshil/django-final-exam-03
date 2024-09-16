from django import forms
from .models import VaccineBooking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class VaccineBookingForm(forms.ModelForm):
    class Meta:
        model = VaccineBooking
        exclude = ["patient"]
        widgets = {
            "vaccine_campaign": forms.HiddenInput(),
            "is_completed": forms.HiddenInput(),
            "date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                    "placeholder": "Select start date and time",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(VaccineBookingForm, self).__init__(*args, **kwargs)
        self.fields["vaccine_campaign"].required = False
        self.fields["is_completed"].required = False
        self.helper = FormHelper(self)
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))
