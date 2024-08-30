from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if  request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    print(username, password)
    if not user:
        messages.success(request, 'Falha no processo de autenticação')
        return redirect('login')
    else:
        auth(request, user)
        return redirect('dashboard')

def register(request):
    return render(request, "register.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def logaut_auth(request):
    logout(request)
    return redirect('login')