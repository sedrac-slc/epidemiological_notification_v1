from backend.entities.concrect.laboratory_technician import LaboratoryTechnician
from backend.service.helper import paginator
from backend.dto.laboratory_technician import create_laboratory_technician, update_laboratory_technician, hidden_laboratory_technician, find_by_id

class LaboratoryTechnicianService:
   
    def findAll(self):
        data = LaboratoryTechnician.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return data
    
    def findAllPage(self, request):
        data = self.findAll()
        return paginator(request, data)
    
    def findById(self, id):
        return find_by_id(id)
    
    def save(self, request):
        return create_laboratory_technician(request)
    
    def update(self, request):
        return update_laboratory_technician(request)
    
    def hidden(self, request):
        return hidden_laboratory_technician(request)