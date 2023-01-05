from django.contrib import admin
from .models import UserModel, EmployeeModel
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'pass1', 'pass2')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'department')


admin.site.register(UserModel, UserAdmin)
admin.site.register(EmployeeModel, EmployeeAdmin)
