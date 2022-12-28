from django import forms


class CheckForm(forms.Form):
    number = forms.FloatField(label='Enter Number')
