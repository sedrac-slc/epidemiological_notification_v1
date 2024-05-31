from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "pages/patient.html", { 'title': 'Paciente'})

def store(request):
    if request.method != "POST": return redirect('patient.index')
    
    messages.success(request, 'Paciente cadastrada com successo!')
    return redirect('patient.index')
   

def update(request):
    if request.method != "POST": return redirect('patient.index') 
    
    messages.success(request, 'Paciente editada com successo!')
    return redirect('patient.index')

def delete(request):
    if request.method != "POST": return redirect('patient.index')
    
    messages.success(request, 'Paciente eliminada com successo!')
    return redirect('patient.index')