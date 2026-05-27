from django.db import models
from appStudent.models import Student

from appFaculty.models import Faculty

from appCourse.models import Course

# Create your models here.
class Attendance(models.Model):
    student=models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    faculty=models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE
    )
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    date = models.DateField(auto_now_add=True)

    present = models.BooleanField(default=False)

    class Meta:
        unique_together=(
            'student',
            'course',
            'date'
        )
    def __str__(self):
        return f"{self.student} - {self.date}"