import time
from django.shortcuts import render, redirect
from . models import UserModel
from django.contrib.auth import authenticate, login, logout
from django . http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import EmployeeModel
from . forms import EmployeeForm
from django.core.paginator import Paginator

# Create your views here.


@login_required(login_url='registration')
def home(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        if request.POST['name' and 'mail' and 'pwd1' and 'pwd2'] == "":
            return render(request, 'registration.html', {'error': True})
        aname = request.POST.get('name')
        email = request.POST.get('mail')
        password1 = request.POST.get('pwd1')
        password2 = request.POST.get('pwd2')
        print(aname, email, password1, password2)
        if password1 != password2:
            return render(request, 'registration.html', {'alert': True})
        elif password1 == password2:
            user = User.objects.create_user(username=aname, email=email, password=password1)
            user.save()
            # messages.success(request, aname + " is added successfully...")
            # return render(request, 'registration.html')
            return redirect('login')
        else:
            return redirect('registration')
    return render(request, 'registration.html')


def login_page(request):
    if request.method == 'POST':
        if request.POST['mail' and 'pass'] == "":
            return render(request, 'login.html', {'error': True})
        uname = request.POST.get('mail')
        password = request.POST.get('pass')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Bad Credentials")
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('registration')


@login_required(login_url='registration')
def add_emp(request):
    if request.method == 'POST':
        if request.POST.get('ename' and 'age' and 'add' and 'dept') == "":
            context = {'error': True}
            return render(request, 'addemp.html', context)
        emp_name=request.POST.get('ename')
        emp_age = request.POST.get('age')
        emp_address = request.POST.get('add')
        emp_department = request.POST.get('dept')
        new_emp = EmployeeModel.objects.create(name=emp_name, age=emp_age, address=emp_address, department=emp_department)
        new_emp.save()
        messages.success(request, emp_name + " is added successfully...")
        return redirect('addem')
    return render(request, 'addemp.html')


@login_required(login_url='registration')
def list_all_employees(request):
    obj = EmployeeModel.objects.all()
    var = list(obj)
    pag = Paginator(var, 2)  # Here we use paginator and set how many records you want on single page
    for i in pag:
        print(i)
    page_number = request.GET.get('page')  # Here we get current page number
    page_obj = pag.get_page(page_number)  # Here we get objects which is present on above page
    for i in page_obj:
        print(i.name, i.age)
    total_pages = pag.num_pages
    print(total_pages)
    inner_page = [n+1 for n in range(total_pages)]
    context = {'output': page_obj, 'innerpages': inner_page}
    return render(request, 'all.html', context)


@login_required(login_url='registration')
def delete_an_employee(request):
    obje = EmployeeModel.objects.all()
    context = {'out': obje}
    return render(request, 'del.html', context)


@login_required(login_url='registration')
def delete_emp_by_id(request, eid):
    try:
        get_employee = EmployeeModel.objects.get(id=eid)
        get_employee.delete()
        return redirect('dele')
    except:
        "Employee Not Found..."
    return redirect('dele')


@login_required(login_url='registration')
def update_an_employee(request):
    ob = EmployeeModel.objects.all()
    context = {'output': ob}
    return render(request, 'update.html', context)


@login_required(login_url='registration')
def update_emp_by_id(request, eid):
    get_emp = EmployeeModel.objects.get(id=eid)
    obj = EmployeeForm(instance=get_emp)
    if request.method == 'POST':
        obj = EmployeeForm(request.POST, instance=get_emp)
        obj.save()
        return redirect('updat')
    for i in obj:
        print(i)
    context = {'data': obj}
    return render(request, 'newupdate.html', context)
