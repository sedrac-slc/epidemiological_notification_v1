from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from backend.entities.concrect.person import genders, maritalStatus
from backend.service.concrect.doctor import DoctorService
from django.http import HttpResponse

doctorService = DoctorService()

# Create your views here.
def index(request):
    data = doctorService.findAllPage(request)
    return render(request, "pages/doctor.html", { 
        'data': data,
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
            doctorService.save(request)
            messages.success(request, 'Médico cadastrada com successo!')
            return redirect('doctor.index')
    except Exception:
        messages.error(request, 'Não foi possível realizar o cadastramento!')
        return redirect('doctor.index')
   

def update(request):
    if request.method != "POST": return redirect('doctor.index') 
    
    messages.success(request, 'Médico editada com successo!')
    return redirect('doctor.index')

def delete(request):
    if request.method != "POST": return redirect('doctor.index')
    
    messages.success(request, 'Médico eliminada com successo!')
    return redirect('doctor.index')