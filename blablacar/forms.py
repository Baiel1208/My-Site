from django import forms

from blablacar.models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ["start_address", "end_address",]