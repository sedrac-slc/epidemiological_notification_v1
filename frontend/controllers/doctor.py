from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from django.http import HttpResponse
from backend.entities.concrect.person import genders, maritalStatus
from backend.dto.user import user_request, person_request

# Create your views here.
def index(request):
    return render(request, "pages/doctor.html", { 
        'title': 'Médico',
        'genders': genders(),
        'maritalStatus' : maritalStatus(),
        'store': reverse('doctor.store'),
        'update': reverse('doctor.update'),
        'delete': reverse('doctor.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('doctor.index')
    try:
        with transaction.atomic():
            user = user_request(request)
            person = person_request(request, user)
            messages.success(request, 'Doctor cadastrada com successo!')
        return redirect('doctor.index')
    except Exception as e:
        messages.error(request, 'Não foi possível realizar o cadastramento!')
        return redirect('doctor.index')
   

def update(request):
    if request.method != "POST": return redirect('doctor.index') 
    
    messages.success(request, 'Doctor editada com successo!')
    return redirect('doctor.index')

def delete(request):
    if request.method != "POST": return redirect('doctor.index')
    
    messages.success(request, 'Doctor eliminada com successo!')
    return redirect('doctor.index')