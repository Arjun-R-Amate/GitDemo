from django import forms


class MarksForms(forms.Form):
    sub1 = forms.IntegerField(label='Subject 1 ')
    sub2 = forms.IntegerField(label='Subject 2 ')
    sub3 = forms.IntegerField(label='Subject 3 ')
    sub4 = forms.IntegerField(label='Subject 4 ')
    sub5 = forms.IntegerField(label='Subject 5 ')
