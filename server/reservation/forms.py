from django import forms

class ReservationForm(forms.Form):
    date = forms.CharField()
    time = forms.CharField()
    length = forms.IntegerField()
    type = forms.CharField()