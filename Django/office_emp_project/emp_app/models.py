from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Department"


class Role(models.Model):
    name = models.CharField(max_length=255, null= False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Role"


class Employee(models.Model):
    first_name = models.CharField(max_length=255, null= False)
    last_name = models.CharField(max_length=255)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    sallary = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        # return f'''{self.__dict__}'''
        return "%s %s %s %s %s" %(self.first_name, self.last_name, self.dept, self.role, self.hire_date)

    def __repr__(self):
        return str(self)
    
    class Meta:
        db_table = "Employee"
