from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.


def register(request):
    context = {}
    if request.method == 'POST':
        try:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "User created successfully!")
                return redirect('honey:users_dashboard')
        except Exception as e:
            form = UserCreationForm()
            context['form'] = form
            messages.error(request, f"Error creating user: username already exists or invalid data.")
            return render(request, 'users/register.html', context)
    else:
        form = UserCreationForm()
    context['form'] = form
    return render(request, 'users/register.html', context)


def login_view(request):
    context = {}
    if request.method == 'POST':
        try:
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('honey:users_dashboard')
            else:
                context['form'] = form
                messages.error(request, "Invalid username or password.")
                return render(request, 'users/login.html', context)
        except Exception as e:
            form = AuthenticationForm()
            context['form'] = form
            messages.error(request, "Invalid username or password.")
            return render(request, 'users/login.html', context)
    else:
        form = AuthenticationForm()
    context['form'] = form
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('honey:home')