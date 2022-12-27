from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cal/', views.calculation, name='calculate'),
    path('final/', views.calculate, name='anser'),
]
