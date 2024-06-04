from backend.entities.concrect.patient import Patient
from backend.service.helper import paginator
from backend.dto.patient import create_patient, update_patient, hidden_patient, find_by_id

class PatientService:
   
    def findAll(self):
        data = Patient.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return data
    
    def findAllPage(self, request):
        data = self.findAll()
        return paginator(request, data)
    
    def findById(self, id):
        return find_by_id(id)
    
    def save(self, request):
        return create_patient(request)
    
    def update(self, request):
        return update_patient(request)
    
    def hidden(self, request):
        return hidden_patient(request)