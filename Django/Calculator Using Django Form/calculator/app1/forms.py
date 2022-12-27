from django import forms


class CalculatorForm(forms.Form):
    value1 = forms.IntegerField(label='Enter Value 1')
    operator = forms.CharField(label='Enter Operator', max_length=10)
    value2 = forms.IntegerField(label='Enter value 2')
