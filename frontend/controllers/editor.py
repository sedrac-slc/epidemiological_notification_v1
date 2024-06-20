from django.shortcuts import render
from backend.service.concrect.medical_record import MedicalRecordService

medicalRecordService = MedicalRecordService()

def index(request,id):
    medical_record = medicalRecordService.findById(id)
    return render(request, "pages/group.html", {
        'medical_record': medical_record
    })