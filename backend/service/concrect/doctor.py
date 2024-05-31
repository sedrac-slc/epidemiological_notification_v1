from backend.entities.concrect.doctor import Doctor
from backend.service.helper import paginator
from django.utils import timezone
from backend.dto.user import create_doctor

class DoctorService:
   
    def findAll(self):
        data = Doctor.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return data
    
    def findAllPage(self, request):
        data = self.findAll()
        return paginator(request, data)
    
    def findById(self, id):
        data = Doctor.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
        return data.first()
    
    def save(self, request):
        return create_doctor(request)
    
    def update(self, data: Doctor):
        data.concat_values_fields()
        Doctor.objects.filter(id = data.id).update(name = data.name, concat_fields = data.concat_fields)
        return data
    
    def remove(self, id):
        data = self.findById(id)
        Doctor.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    