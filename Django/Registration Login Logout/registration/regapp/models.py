from django.db import models

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=100)
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)

    class Meta:
        db_table = 'USER'


class EmployeeModel(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    address = models.CharField(max_length=250)
    department = models.CharField(max_length=150)

    class Meta:
        db_table = 'Employee_Master'
