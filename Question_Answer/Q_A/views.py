from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render

from . import forms

# Create your views here.

# Index view
def index(response):
    return HttpResponse("<h1> Ceci est un site web </h1>")

# Authentification formulaire

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = auto.save()
            login(request, user)
            return redirect(setting.LOGIN_REDIRECT_URL)

    return render(request, 'site/signup.html', context = {'form' : form})
