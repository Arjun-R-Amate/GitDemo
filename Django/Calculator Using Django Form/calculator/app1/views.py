from django.shortcuts import render
from . forms import CalculatorForm
from django . http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'index.html')


def calculate(request):
    variable = CalculatorForm()
    result = 0
    if request.method == 'POST':
        num1 = eval(request.POST.get("value1"))
        num2 = eval(request.POST.get("value2"))
        operator = request.POST.get("operator")
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            return HttpResponse('Invalid Inputs')
    context = {'forms': variable, 'output': '{:.2f}'.format(result)}
    return render(request, 'calculate.html', context)
