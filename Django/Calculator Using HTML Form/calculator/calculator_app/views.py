from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Welcome to our calculator using html form")


def calculation(request):
    result = 0
    try:
        if request.method == 'POST':
            number1 = int(request.POST['val1'])
            number2 = int(request.POST['val2'])
            operator = request.POST['opr']
            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2
            elif operator == '*':
                result = number1 * number2
            elif operator == '/':
                result = number1 / number2
            else:
                return HttpResponse("Invalid inputs")
    except:
        return Exception
    context = {'finalans': "{:.2f}".format(result), 'title': 'self company'}
    return render(request, 'forms.html', context)


def calculate(request):
    answer = 0
    try:
        if request.method == 'POST':
            num1 = int(request.POST["val1"])
            num2 = int(request.POST["val2"])
            operator = request.POST["opr"]
            if operator == '+':
                answer = num1 + num2
            elif operator == '-':
                answer = num1 - num2
            elif operator == '*':
                answer = num1 * num2
            elif operator == '/':
                answer = num1 / num2
            else:
                return HttpResponse("Invalid Inputs...")
    except:
        return HttpResponse("Program error")
    context = {'result': '{:.2f}'.format(answer)}
    return render(request, 'calculate.html', context)
