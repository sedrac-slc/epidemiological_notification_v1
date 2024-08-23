from backend.entities.concrect.patient import Patient
from backend.service.concrect.person import PersonService
from backend.service.concrect.institution import InstitutionService
from backend.service.helper import paginator
from backend.dto.patient import create_patient, update_patient, hidden_patient, find_by_id
from backend.utils.data import save_model

personService = PersonService()
institutionService = InstitutionService()

class PatientService:
   
    def findAll(self):
        return Patient.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
    
    def findAllPage(self, request):
        return paginator(request, self.findAll())
    
    def findById(self, id):
        return find_by_id(id)
    
    def findByPerson(self, patient: Patient):
        return Patient.objects.filter(person = patient.person, deleted_at__isnull=True, deleted_by__isnull=True).first()    
        
    def findAllByPatient(self, id):
        institution = institutionService.findById(id)
        return Patient.objects.filter(person__institution = institution, deleted_at__isnull=True, deleted_by__isnull=True).all()
        
    def findOrSave(self, data: Patient):
        patient = self.findByPerson(data)        
        if patient != None: 
            return patient
        return save_model(data)
            
    def save(self, request):
        return create_patient(request)
    
    def update(self, request):
        return update_patient(request)
    
    def hidden(self, request):
        return hidden_patient(request)