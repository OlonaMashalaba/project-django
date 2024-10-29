from django.shortcuts import render, get_object_or_404
from .models import Candidate

def home(request):
    return render(request, 'candidates/home.html')

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidate_list.html', {'candidates': candidates})

def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    return render(request, 'candidates/candidate_detail.html', {'candidate': candidate})


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('candidates:home'))
        else:
            return render(request, 'candidates/login.html', {'error': 'Invalid credentials'})
    return render(request, 'candidates/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('candidates:home'))

def add(a, b):
    """Adds two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b
