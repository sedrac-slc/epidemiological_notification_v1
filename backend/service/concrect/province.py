from backend.entities.concrect.province import Province
from backend.service.helper import paginator
from django.utils import timezone

class ProvinceService:
   
    def findAll(self):
        return Province.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        return paginator(request, self.findAll())
    
    def findById(self, id):
        return Province.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return Province.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Province):
        province = self.findByName(data.name)
        if province != None: 
            return province
        return self.save(data)
    
    def save(self, data: Province):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: Province):
        data.concat_values_fields()
        Province.objects.filter(id = data.id).update(name = data.name, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Province.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    