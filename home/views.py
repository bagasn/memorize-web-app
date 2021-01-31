from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as func_login, logout

from .forms import Login as FormLogin


def index(request):
    logout(request)
    return redirect(login)


def login(request):
    form = FormLogin()
    if request.method == "POST":
        form = FormLogin(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        auth = authenticate(request, username=username, password=password)
        print(auth)
        if auth is not None:
            func_login(request, auth)
            return redirect(home)
        else:
            print("Login failed!")

    context = {
        'page_title': 'Login',
        'form_login': form,
    }
    return render(request, 'login.html', context)


def home(request):
    context = {
        'page_title': 'Home',
        'data': request.user
    }
    return render(request, 'home.html', context)


def debug_view(request):
    context = {
        'data': request.user,
    }
    return render(request, 'debug_view.html', context)

