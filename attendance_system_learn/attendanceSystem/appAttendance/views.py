from django.shortcuts import render,redirect

# Create your views here.
from .forms import AttendanceForm

from appStudent.models import Student
from appAttendance.models import Attendance

from datetime import date


def mark_attendance(request):

    students = []

    if request.method == "POST":

        course_id = request.POST.get("course")

        students = Student.objects.filter(
            course_id=course_id
        )

        selected_students = request.POST.getlist(
            "students"
        )

        if selected_students:

            for sid in selected_students:

                Attendance.objects.get_or_create(

                    student_id=sid,

                    course_id=course_id,

                    date=date.today(),

                    defaults={

                        'faculty_id': 1,
                        'present': True
                    }
                )

            return redirect('/attendance/')

    form = AttendanceForm()

    return render(

        request,

        'attendance/mark_attendance.html',

        {
            'form': form,
            'students': students
        }
    )