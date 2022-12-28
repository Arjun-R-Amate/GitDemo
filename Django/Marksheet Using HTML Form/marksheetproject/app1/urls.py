from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marks/', views.calculate_marks, name='marks'),
]
