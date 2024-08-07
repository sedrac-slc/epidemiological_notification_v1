from backend.entities.concrect.zone import Zone
from backend.service.helper import paginator
from django.utils import timezone

class ZoneService:
   
    def findAll(self):
        return Zone.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        return paginator(request, self.findAll())
    
    def findById(self, id):
        return Zone.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return Zone.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Zone):
        province = self.findByName(data.name)
        if province != None: 
            return province
        return self.save(data)
    
    def save(self, data: Zone):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: Zone):
        data.concat_values_fields()
        Zone.objects.filter(id = data.id).update(name = data.name, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Zone.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    