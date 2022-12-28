from django.shortcuts import render
from . forms import CheckForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


def even_odd(request):
    val = CheckForm()
    result = ""
    number = ""
    try:
        if request.method == 'POST':
            number = eval(request.POST.get('number'))
            if number % 2 == 0:
                result = "This is EVEN number"
            else:
                result = "This is ODD number"
    except:
        result = "Unknown values"
    context = {'input_value': val, 'output': result, 'number': number}
    return render(request, 'eveod.html', context)
