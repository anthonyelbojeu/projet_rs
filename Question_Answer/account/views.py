import datetime

from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth import logout
#Pour gérer les permissions
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.models import AbstractUser, Group


from .forms import UserRegistrationForm, UserLoginForm

from django.contrib.auth.models import AbstractUser, Group

from .models import User


from . import forms

# Create your views here.

# Index view
def index(response):
    return HttpResponse("<h1> Ceci est un templates web </h1>")



# Authentification formulaire

#def SignupPage(request):
#    form = forms.SignupForm()
#    if request.method == 'POST':
#        form = forms.SignupForm(request.POST)
#        if form.is_valid():
#            user = auto.save()
#            login(request, user)
#            return redirect(setting.LOGIN_REDIRECT_URL)
#
#    return render(request, 'templates/signup.html', context = {'form' : form})

class UserCreateView(View):
    html_template = 'signup.html'

    def get(self, request):
        context = {}
        context['form'] = UserRegistrationForm() # equivaut à context = {'form': UserLoginForm()}
        return render(request, self.html_template, context)

    def post(self, request):
        context = {}
        context['form'] = UserRegistrationForm()
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if email == '':
            messages.error(request, "vous n'avez pas renseigné de mail")
        elif username == '':
            messages.error(request, "vous n'avez pas renseigné d'usurname")
        elif password1 == '':
            messages.error(request, "vous n'avez pas renseigné de mot de passe1")
        elif password2 == '':
            messages.error(request, "vous n'avez pas renseigné de mot de passe1")
        elif password1 != password2:
            messages.error(request, "Vos mots de passe sont différents")
        if User.objects.filter(username=username).exists():
             messages.error(request, "le nom d'utilisateur existe déjà")
        elif User.objects.filter(email=email).exists():
             messages.error(request, "le nom d'utilisateur existe déjà")
        else:
            user = User.objects.create_user(username=username , password=password1, email=email)
            #attribution du groupe quand la perosnne crée le compte. le groupe visitor existe déjàç en admin.
            #group = Group.objects.get(name='visitor')
            #user.groups.add(group)
            auth.login(request, user)
            return redirect('account:index')
        return render(request, self.html_template, context)



class UserLoginView(View):
    html_template = 'login.html'

    def get(self, request):
        context = {}
        context['form'] = UserLoginForm()
        return render(request, self.html_template, context)

    def post(self, request):
        context = {}
        context['form'] = UserLoginForm()
        username = request.POST['username']
        password = request.POST['password']
        if username == '':
            messages.errors(request, "vous n'avez pas renseigné d'usurname")
            return render(request, self.html_template, context)
        elif password == '':
            messages.errors(request, "vous n'avez pas renseigné de mot de passe")
            return render(request, self.html_template, context)
        else:
            user= auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Vous avez été connecté avec succés")
                #group = Group(name="pdg")
                #if user.groups.filter(name=group):
                #    print("caca")
                #    return redirect('redacteur:redacteur-connect')

                return redirect('account:index')

            else:
                messages.error(request, "Vous n'avez pas pu être connecté")
                return render(request, self.html_template, context)


