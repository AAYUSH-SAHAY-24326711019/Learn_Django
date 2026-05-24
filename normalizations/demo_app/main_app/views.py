from django.shortcuts import render, redirect

from appA.models import ModelA
from appB.models import ModelB
from .models import MainModel


def first_page(request):

    if request.method == "POST":

        emp_id = request.POST.get("emp_id")
        dept_id = request.POST.get("dept_id")

        emp_obj = ModelA.objects.get(id=emp_id)
        dept_obj = ModelB.objects.get(id=dept_id)

        MainModel.objects.create(
            emp=emp_obj,
            dept=dept_obj
        )

        return redirect('/')

    data = MainModel.objects.all()

    context = {
        'data': data
    }

    return render(request, 'main_app/first_page.html', context)