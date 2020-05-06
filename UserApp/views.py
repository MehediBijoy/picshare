from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView

from . import models
from . forms import UserRegisterForm


def profileView(request, username):
    return render(request, 'Profile.html', {'username': username})


class loginView(LoginView):
    template_name = 'Login.html'


class logoutView(LogoutView):
    template_name = 'Logout.html'


def UserRegistration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Registration.html', {'form': form})
