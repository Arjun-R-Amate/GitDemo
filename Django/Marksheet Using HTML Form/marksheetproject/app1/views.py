from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def calculate_marks(request):
    total = ""
    percentage = ""
    division = ""
    try:
        if request.method == 'POST':
            subject1 = eval(request.POST['sub1'])
            subject2 = eval(request.POST['sub2'])
            subject3 = eval(request.POST['sub3'])
            subject4 = eval(request.POST['sub4'])
            subject5 = eval(request.POST['sub5'])
            total = subject1 + subject2 + subject3 + subject4 + subject5
            print(total)
            percentage = total*100 / 500
            if percentage > 75:
                division = "Distinction"
            elif percentage > 60:
                division = "First Class"
            elif percentage > 50:
                division = "Second Class"
            elif percentage > 35:
                division = "Pass"
            else:
                division = "Fail"
    except:
        pass
    context = {'marks': total, 'percent': percentage, 'div': division}
    return render(request, 'marksheet.html', context)
