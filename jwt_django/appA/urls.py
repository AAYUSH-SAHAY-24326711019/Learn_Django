from django.urls import path

from .views import login_view, dashboard

urlpatterns = [

    path('', login_view),

    path('dashboard/', dashboard),
]