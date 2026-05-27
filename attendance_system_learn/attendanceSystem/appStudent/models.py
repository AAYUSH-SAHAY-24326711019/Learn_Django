from django.db import models
from appCourse.models import Course

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname