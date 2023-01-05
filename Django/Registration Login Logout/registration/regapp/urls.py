from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='registration'),
    path('login/', views.login_page, name='login'),
    path('add/', views.add_emp, name='addem'),
    path('all/', views.list_all_employees, name='allemp'),
    path('delete/', views.delete_an_employee, name='dele'),
    path('delete/<int:eid>', views.delete_emp_by_id, name='delete'),
    path('update/', views.update_an_employee, name='updat'),
    path('update/<int:eid>', views.update_emp_by_id, name='update'),
]
