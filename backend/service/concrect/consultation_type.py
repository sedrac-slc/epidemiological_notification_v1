from backend.entities.concrect.consultation_type import ConsultationType
from backend.service.helper import paginator
from django.utils import timezone

class ConsultationTypeService:
   
    def findAll(self):
        return ConsultationType.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        return paginator(request, self.findAll())
    
    def findById(self, id):
        return ConsultationType.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return ConsultationType.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: ConsultationType):
        consultationType = self.findByName(data.name)
        if consultationType != None: 
            return consultationType
        return self.save(data)
    
    def save(self, data: ConsultationType):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: ConsultationType):
        data.concat_values_fields()
        ConsultationType.objects.filter(id = data.id).update(name = data.name, price = data.price, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        ConsultationType.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    