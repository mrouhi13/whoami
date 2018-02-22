from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'profile/index.html')


def profile(request):
    return render(request, 'profile/profile.html')


def signup(request):
    return render(request, 'profile/registration/signup.html')


def signin(request):
    return render(request, 'profile/registration/signin.html')


def password_reset(request):
    return render(request, 'profile/registration/password_reset.html')


def password_reset_confirm(request):
    return render(request, 'profile/registration/password_reset_confirm.html')
