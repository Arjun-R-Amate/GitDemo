from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Welcome to our calculator using html form")


def calculation(request):
    result = 0
    number1 = ""
    number2 = ""
    try:
        if request.method == 'POST':
            number1 = eval(request.POST['val1'])
            number2 = eval(request.POST['val2'])
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
    context = {'finalans': "{:.2f}".format(result), 'title': 'self company', 'num1': number1, 'num2': number2}
    return render(request, 'forms.html', context)


def calculate(request):
    '''
    Here usage select tag in html name used as operator and value tag is used input
    '''
    answer = 0
    num1 = ""
    num2 = ""
    try:
        if request.method == 'POST':
            num1 = eval(request.POST["val1"])
            num2 = eval(request.POST["val2"])
            operator = request.POST["opr"]
            print(operator)
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
    context = {'result': '{:.2f}'.format(answer), 'num1': num1, 'num2': num2, 'Title': 'Company Name'}
    return render(request, 'calculate.html', context)
