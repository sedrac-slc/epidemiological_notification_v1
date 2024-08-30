from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from backend.entities.concrect.person import genders, maritalStatus
from backend.service.concrect.patient import PatientService
from backend.service.concrect.institution import InstitutionService

patientService = PatientService()
institutionService = InstitutionService()
# Create your views here.
@login_required
def index(request):
    institutions = institutionService.findAll()
    data = patientService.findAllPage(request)
    return render(request, "pages/patient.html", { 
        'data': data,
        'title': 'Pacientes',
        'genders': genders(),
        'maritalStatus': maritalStatus(),
        'institutions': institutions,
        'store': reverse('patient.store'),
        'update': reverse('patient.update'),
        'delete': reverse('patient.delete') 
    })

@login_required
def store(request):
    if request.method != "POST": return redirect('patient.index')
    try:
        with transaction.atomic():
            patientService.save(request)
            messages.success(request, 'Paciente cadastrada com successo!')
    except Exception as e:
        print(e)
        messages.error(request, 'Não foi possível realizar o cadastramento!')
    return redirect('patient.index')
   
@login_required
def update(request):
    if request.method != "POST": return redirect('patient.index')
    try:
        with transaction.atomic():
            patientService.update(request)
            messages.success(request, 'Paciente editada com successo!')
    except Exception:
        messages.error(request, 'Não foi possível realizar o edição!')
    return redirect('patient.index')
    
@login_required
def delete(request):
    if request.method != "POST": return redirect('patient.index')
    try:
        with transaction.atomic():
            patientService.hidden(request)
            messages.success(request, 'Paciente eliminada com successo!')
    except Exception:
        messages.error(request, 'Não foi possível realizar o eliminação!')
    return redirect('patient.index')