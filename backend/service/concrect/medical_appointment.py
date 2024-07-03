from backend.entities.concrect.medical_appointment import MedicalAppointment
from backend.service.concrect.patient import PatientService
from backend.service.helper import paginator
from django.utils import timezone

petientService = PatientService()

class MedicalAppointmentService:

    def list(self):
        return MedicalAppointment.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return MedicalAppointment.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return MedicalAppointment.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()    

    def findAllByPatient(self, id):
        patient = petientService.findById(id)
        return MedicalAppointment.objects.filter(patient = patient, deleted_at__isnull=True, deleted_by__isnull=True).all()
        
    def save(self, data: MedicalAppointment):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: MedicalAppointment):
        data.concat_values_fields()
        MedicalAppointment.objects.filter(id = data.id).update(accomplished = data.accomplished, description = data.description, patient = data.patient, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        MedicalAppointment.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data  