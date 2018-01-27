from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'profile/index.html')


def profile(request):
    return render(request, 'profile/profile.html')


def signup(request):
    return render(request, 'profile/signup.html')


def signin(request):
    return render(request, 'profile/signin.html')


def recover_password(request):
    return render(request, 'profile/recover_password.html')


def agreement(request):
    return render(request, 'profile/agreement.html')
