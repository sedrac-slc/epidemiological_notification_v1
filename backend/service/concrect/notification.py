from backend.entities.concrect.notification import Notification
from .laboratory_technician import LaboratoryTechnicianService
from .institution import InstitutionService
from .sickness import SicknessService
from .patient import PatientService
from backend.service.helper import paginator
from django.utils import timezone

patientService = PatientService()
sicknessService = SicknessService()
institutionService = InstitutionService()
laboratoryTechnicianService = LaboratoryTechnicianService()

class NotificationService:

    def list(self):
        return Notification.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
    
    def findAll(self):
        return self.list().all()
        
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return Notification.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()

    def findAllByPatient(self, id):
        patient = patientService.findById(id)
        return Notification.objects.filter(patient = patient, deleted_at__isnull=True, deleted_by__isnull=True).all()
    
    def findAllBySickness(self, id):
        sickness = sicknessService.findById(id)
        return Notification.objects.filter(sickness = sickness, deleted_at__isnull=True, deleted_by__isnull=True).all()

    def findAllByInstitution(self, id):
        institution = institutionService.findById(id)
        return Notification.objects.filter(institution = institution, deleted_at__isnull=True, deleted_by__isnull=True).all()

    def findAllByLaboratoryTechnician(self, id):
        laboratoryTechnician = laboratoryTechnicianService.findById(id)
        return Notification.objects.filter(laboratoryTechnician = laboratoryTechnician, deleted_at__isnull=True, deleted_by__isnull=True).all()    
    
    def findOrSave(self, data: Notification):
        Notification = self.findByName(data.name)
        if Notification != None: 
            return Notification
        return self.save(data)    
        
    def save(self, data: Notification):
        self.valied(data)
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: Notification):
        self.valied(data)
        data.concat_values_fields()
        Notification.objects.filter(id = data.id).update(name = data.name, province = data.province, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Notification.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data
    
    def valied(self, data: Notification):
        patient = patientService.findById(data.patient.id)
        sickness = sicknessService.findById(data.sickness.id)
        institution = institutionService.findById(data.institution.id)
        laboratoryTechnician = laboratoryTechnicianService.findById(data.laboratoryTechnician.id)
        return Notification.objects.filter(
            patient=patient, 
            sickness=sickness, 
            institution=institution, 
            laboratoryTechnician=laboratoryTechnician,
            deleted_at__isnull=True, 
            deleted_by__isnull=True
        ).first()