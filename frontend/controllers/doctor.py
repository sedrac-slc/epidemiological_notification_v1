from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from backend.entities.concrect.person import genders, maritalStatus
from backend.service.concrect.doctor import DoctorService
from backend.service.concrect.institution import InstitutionService

doctorService = DoctorService()
institutionService = InstitutionService()

# Create your views here.
def index(request):
    institutions = institutionService.findAll()
    data = doctorService.findAllPage(request)
    return render(request, "pages/doctor.html", { 
        'data': data,
        'title': 'Médico',
        'genders': genders(),
        'maritalStatus': maritalStatus(),
        'institutions': institutions,
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
    except Exception as e:
        messages.error(request, 'Não foi possível realizar o cadastramento!')
    return redirect('doctor.index')
   

def update(request):
    if request.method != "POST": return redirect('doctor.index')
    try:
        with transaction.atomic():
            doctorService.update(request)
            messages.success(request, 'Médico editada com successo!')
    except Exception:
        messages.error(request, 'Não foi possível realizar o edição!')
    return redirect('doctor.index')
    
def delete(request):
    if request.method != "POST": return redirect('doctor.index')
    try:
        with transaction.atomic():
            doctorService.hidden(request)
            messages.success(request, 'Médico eliminada com successo!')
    except Exception:
        messages.error(request, 'Não foi possível realizar o eliminação!')
    return redirect('doctor.index')