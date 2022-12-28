from django.shortcuts import render
from django .http import HttpResponse
from . forms import MarksForms
# Create your views here.


def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Works perfect...")


def calculate_marks(request):
    marks = MarksForms()
    total = ""
    percent = ""
    division = ""
    try:
        if request.method == "POST":
            s1 = eval(request.POST.get('sub1'))
            s2 = eval(request.POST.get('sub2'))
            s3 = eval(request.POST.get('sub3'))
            s4 = eval(request.POST.get('sub4'))
            s5 = eval(request.POST.get('sub5'))
            total = s1 + s2 + s3 + s4 + s5
            percent = total*100 / 500
            if percent > 75 :
                division = "Distinction"
            elif percent > 60:
                division = "First-Class"
            elif percent > 50:
                division = "Second-Class"
            elif percent > 35:
                division = "Pass"
            else:
                division = "Fail"
    except:
        pass
    context = {'mark': marks, 'total_marks': total, 'percentage': percent, 'div': division}
    return render(request, 'marksheet.html', context)
