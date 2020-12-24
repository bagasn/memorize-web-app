from django.shortcuts import render


def index(request):
    context = {
        "page_title": "Login",
    }
    return render(request, 'login.html', context)

