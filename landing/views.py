from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def index(request):
    return render(request, 'landing/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            context = {'error': 'Invalid email or password'}
            return render(request, 'landing/login.html', context)
    else:
        return render(request, 'landing/login.html')