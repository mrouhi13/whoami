from django.shortcuts import render


def index(request):
    return render(request, 'accounts/index.html')


def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    return render(request, 'accounts/registration/signup.html')


def profile_activate(request):
    return render(request, 'accounts/registration/profile_activate.html')


def signin(request):
    return render(request, 'accounts/registration/signin.html')


def password_reset(request):
    return render(request, 'accounts/registration/password_reset.html')


def password_reset_confirm(request):
    return render(request, 'accounts/registration/password_reset_confirm.html')
