from django import forms

class ReservationForm(forms.Form):
    date = forms.CharField()
    time = forms.CharField()
    type = forms.CharField()