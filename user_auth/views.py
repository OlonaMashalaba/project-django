from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']

        User.objects.create_user(username=username, password=password, first_name=first_name)
        return HttpResponseRedirect(reverse('user_auth:login'))
    return render(request, 'authentication/signup.html')



from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('candidates:home'))
        else:
            return HttpResponseRedirect(reverse('user_auth:login'))
def user_login(request):
    return render(request,'authentication/login.html')
