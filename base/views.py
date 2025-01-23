from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *

@login_required(login_url="user_login")
@admin_only
def home(request):
    user_list = User.objects.all()

    return render(request, 'base/home.html', {'user_list':user_list})

@unauthorized_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('home')
        else:
            if user is None:
                messages(request, 'Username not exist')
            else:
                messages(request, 'Password Incorrect')

    return render(request, 'base/authentication/login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

@unauthorized_user
def user_register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'You successfuly registered!')
            return redirect('user_login')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        reg_form = RegForm()
    context = {
        'reg_form': reg_form
    }
    return render(request, 'base/authentication/register.html', context)