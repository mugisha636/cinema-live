from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from . import models
from . import forms

# Create your views here.


def home_page(request):
    global submittedMessage
    submittedMessage = False
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        text = request.POST['text']
        msg = models.Messages.objects.create(
            email=email, subject=subject, text=text)
        msg.save()
        submittedMessage = True

    aboutContents = models.About.objects.all()
    activities = models.WhatWeDo.objects.all().order_by('-date')[:3]
    teamMembers = models.Team.objects.all()
    blogs = models.Blog.objects.all().order_by('-date')[:3]

    context = {
        'aboutContents': aboutContents,
        'activities': activities,
        'teamMembers': teamMembers,
        'blogs': blogs,
        'submittedMessage': submittedMessage
    }
    return render(request, 'index.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(
                        request, f"You are now logged in as {username}")
                    return redirect('/')
                else:
                    messages.warning(
                        request, "Invalid username or password. Try again later")
            else:
                messages.warning(
                    request, "Invalid username or password. Try again later")

        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def register(req):
    if req.user.is_authenticated:
        return redirect('home')
    else:
        if req.method == "POST":
            # defaut django form with only username and password
            # form = UserCreationForm(req.POST)

            # our own customized form from forms.py
            form = forms.UserRegisterForm(req.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    req, f'Hello {username}, your account was created successfull!')
                return redirect('register')

        else:
            # defaut django form with only username and password
            # form = UserCreationForm(req.POST)

            # our own customized form from forms.py
            form = forms.UserRegisterForm()

        return render(req, 'register.html', {'form': form})
