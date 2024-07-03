from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.patient import PatientService
from backend.service.concrect.medical_appointment import MedicalAppointmentService
from backend.dto.medical_appointment import to_medical_appointment , to_medical_appointment_model

patientService = PatientService()
medicalAppointmentService = MedicalAppointmentService()

# Create your views here.
def index(request):
    patients = patientService.findAll()
    data = medicalAppointmentService.findAllPage(request)
    return render(request, "pages/medical-appointment.html", { 
        'data': data, 
        'title': 'Consulta',
        'patients': patients,
        'store': reverse('medical_appointment.store'),
        'update': reverse('medical_appointment.update'),
        'delete': reverse('medical_appointment.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('medical_appointment.index')
    medicalAppointmentService.save(to_medical_appointment(request))
    messages.success(request, 'Consulta cadastrada com successo!')
    return redirect('medical_appointment.index')
   
def update(request):
    if request.method != "POST": return redirect('medical_appointment.index') 
    medicalAppointmentService.update(to_medical_appointment_model(request))
    messages.success(request, 'Consulta editada com successo!')
    return redirect('medical_appointment.index')

def delete(request):
    if request.method != "POST": return redirect('medical_appointment.index')
    medicalAppointmentService.hidden(request.POST.get('model'))
    messages.success(request, 'Consulta eliminada com successo!')
    return redirect('medical_appointment.index')