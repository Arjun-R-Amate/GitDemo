from django.shortcuts import render
from django . http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome to check EVEN/ODD number")


def about(request):
    return render(request, 'index.html')


def even_odd(request):
    result = ""
    number = ""
    title = "Company Name"
    try:
        if request.method == "POST":
            number = eval(request.POST['num'])
            if number % 2 == 0:
                result = "The given number is EVEN."
            else:
                result = "The given number is ODD"
    except:
        pass
    context = {'output': result, "number": number, 'Title': title}
    return render(request, 'check.html', context)
