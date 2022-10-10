from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name')
    price = forms.IntegerField()
    info = forms.CharField()
    length = forms.IntegerField()
    image = forms.CharField()