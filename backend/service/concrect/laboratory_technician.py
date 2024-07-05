from backend.entities.concrect.laboratory_technician import LaboratoryTechnician
from backend.service.helper import paginator
from backend.dto.laboratory_technician import create_laboratory_technician, update_laboratory_technician, hidden_laboratory_technician, find_by_id
from backend.utils.data import save_model

class LaboratoryTechnicianService:
   
    def list(self):
        return LaboratoryTechnician.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
    
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return find_by_id(id)
    
    def findByPerson(self, laboratoryTechnician: LaboratoryTechnician):
        return LaboratoryTechnician.objects.filter(person = laboratoryTechnician.person, deleted_at__isnull=True, deleted_by__isnull=True).first()    
            
    def findOrSave(self, data: LaboratoryTechnician):
        patient = self.findByPerson(data)        
        if patient != None: 
            return patient
        return save_model(data)    
    
    def save(self, request):
        return create_laboratory_technician(request)
    
    def update(self, request):
        return update_laboratory_technician(request)
    
    def hidden(self, request):
        return hidden_laboratory_technician(request)