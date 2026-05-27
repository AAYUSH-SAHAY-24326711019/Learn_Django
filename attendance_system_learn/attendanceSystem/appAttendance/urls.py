from django.urls import path
from .views import mark_attendance

urlpatterns = [

    path(
        '',
        mark_attendance
    ),
]