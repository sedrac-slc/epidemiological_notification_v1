from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.utils.html import escape
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.medical_record import MedicalRecordService
from backend.dto.medical_record import to_medical_record , to_medical_record_model

sicknessService = SicknessService()
medicalRecordService = MedicalRecordService()

# Create your views here.
def index(request):
    sicknesies = sicknessService.findAll()
    data = medicalRecordService.findAllPage(request)
    return render(request, "pages/medical-record.html", { 
        'data': data, 
        'title': 'Ficha médica',
        'sicknesies': sicknesies,
        'store': reverse('medical_record.store'),
        'update': reverse('medical_record.update'),
        'delete': reverse('medical_record.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('medical_record.index')
    medicalRecordService.save(to_medical_record(request))
    messages.success(request, 'Ficha médica cadastrada com successo!')
    return redirect('medical_record.index')
   
def update(request):
    if request.method != "POST": return redirect('medical_record.index') 
    medicalRecordService.update(to_medical_record_model(request))
    messages.success(request, 'Ficha médica editada com successo!')
    return redirect('medical_record.index')

def delete(request):
    if request.method != "POST": return redirect('medical_record.index')
    medicalRecordService.hidden(request.POST.get('model'))
    messages.success(request, 'Ficha médica eliminada com successo!')
    return redirect('medical_record.index')    

def sickness(request):
    medical_records = []
    medical_record = request.GET.get('medical_record','')
    medical_records = medicalRecordService.findAllBySickness(request.GET.get('sickness'))
    data = ''.join([
        f'<option value="{escape(i.id)}" {"selected" if str(i.id) == escape(medical_record) else ""}>{escape(i.name)}</option>'
        for i in medical_records
    ])
    return HttpResponse(data, content_type="text/html;charset=utf-8")