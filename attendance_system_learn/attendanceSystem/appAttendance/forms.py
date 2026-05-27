from django import forms
from appCourse.models import Course


class AttendanceForm(forms.Form):

    course = forms.ModelChoiceField(
        queryset=Course.objects.all()
    )