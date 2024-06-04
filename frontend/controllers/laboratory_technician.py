from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.db import transaction
from backend.entities.concrect.person import genders, maritalStatus
from backend.service.concrect.laboratory_technician import LaboratoryTechnicianService

laboratoryTechnicianService = LaboratoryTechnicianService()

# Create your views here.
def index(request):
    data = laboratoryTechnicianService.findAllPage(request)
    return render(request, "pages/laboratory-technician.html", { 
        'data': data,
        'title': 'Técnicos de laboratórios',
        'genders': genders(),
        'maritalStatus' : maritalStatus(),
        'store': reverse('laboratory_technician.store'),
        'update': reverse('laboratory_technician.update'),
        'delete': reverse('laboratory_technician.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('laboratory_technician.index')
    try:
        with transaction.atomic():
            laboratoryTechnicianService.save(request)
            messages.success(request, 'Técnico de laboratório cadastrada com successo!')
    except Exception:
        messages.error(request, 'Não foi possível realizar o cadastramento!')
    return redirect('laboratory_technician.index')
   

def update(request):
    if request.method != "POST": return redirect('laboratory_technician.index')
    try:
        with transaction.atomic():
            laboratoryTechnicianService.update(request)
            messages.success(request, 'Técnico de laboratório editada com successo!')
    except Exception:
        messages.error(request, 'Não foi possível realizar o edição!')
    return redirect('laboratory_technician.index')
    

def delete(request):
    if request.method != "POST": return redirect('laboratory_technician.index')
    try:
        with transaction.atomic():
            laboratoryTechnicianService.hidden(request)
            messages.success(request, 'Técnico de laboratório eliminada com successo!')
    except Exception:
        messages.error(request, 'Não foi possível realizar o eliminação!')
    return redirect('laboratory_technician.index')