from backend.entities.concrect.doctor import Doctor
from backend.service.helper import paginator
from backend.dto.doctor import create_doctor, update_doctor, hidden_doctor, find_by_id

class DoctorService:
   
    def findAll(self):
        data = Doctor.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return data
    
    def findAllPage(self, request):
        data = self.findAll()
        return paginator(request, data)
    
    def findById(self, id):
        return find_by_id(id)
    
    def save(self, request):
        return create_doctor(request)
    
    def update(self, request):
        return update_doctor(request)
    
    def hidden(self, request):
        return hidden_doctor(request)