from backend.entities.concrect.patient import Patient
from backend.entities.concrect.sickness import Sickness
from backend.entities.concrect.institution import Institution
from backend.entities.concrect.notification import Notification
from backend.entities.concrect.laboratory_technician import LaboratoryTechnician
from backend.service.concrect.patient import PatientService
from backend.service.concrect.laboratory_technician import LaboratoryTechnicianService

patientService = PatientService()
laboratoryTechnicianService = LaboratoryTechnicianService()

def to_notification(request):
    patient = patientService.findById(id = request.POST.get('patient'))
    laboratory_technician = laboratoryTechnicianService.findById(request.POST.get('laboratoryTechnician'))

    sickness = Sickness(id = request.POST.get('sickness'))
    institution = Institution(id = request.POST.get('institution'))
    data = Notification(
        patient = patient,
        sickness = sickness,
        institution = institution,
        laboratoryTechnician = laboratory_technician,
        
        vaccinationDate = request.POST.get('vaccinationDate'),
        observationDate = request.POST.get('observationDate'),
        notificationDate = request.POST.get('notificationDate'),
        manifestationDate = request.POST.get('manifestationDate'),
        
        situation = request.POST.get('situation'),
        classification = request.POST.get('classification'),
        numberOfVaccines = request.POST.get('numberOfVaccines'),
    )
    return data

def to_notification_model(request):
    data = to_notification(request)
    data.id = request.POST.get('model')
    return data