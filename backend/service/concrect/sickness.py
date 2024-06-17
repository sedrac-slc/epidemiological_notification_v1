from backend.entities.concrect.sickness import Sickness
from backend.service.helper import paginator
from django.utils import timezone

class SicknessService:
   
    def findAll(self):
        data = Sickness.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return data
    
    def findAllPage(self, request):
        data = self.findAll()
        return paginator(request, data)
    
    def findById(self, id):
        return Sickness.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return Sickness.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Sickness):
        scickness = self.findByName(data.name)
        if scickness != None: 
            return scickness
        return self.save(data)
    
    def save(self, data: Sickness):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: Sickness):
        data.concat_values_fields()
        Sickness.objects.filter(id = data.id).update(name = data.name, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Sickness.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    