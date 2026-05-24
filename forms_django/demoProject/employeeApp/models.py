# Create your models here.
from django.db import models

class Employee(models.Model):

    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name