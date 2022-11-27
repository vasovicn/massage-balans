from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name')
    info = forms.CharField()
    image = forms.CharField()