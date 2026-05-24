

# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            access_token = str(refresh.access_token)

            request.session['access_token'] = access_token

            return redirect('/dashboard/')

    return render(request,'login.html')


def dashboard(request):

    token = request.session.get('access_token')

    if not token:

        return redirect('/')

    return render(request,'dashboard.html')
