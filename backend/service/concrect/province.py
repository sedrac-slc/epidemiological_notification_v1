from backend.entities.concrect.province import Province
from backend.service.helper import paginator
from django.utils import timezone

class ProvinceService:
    
    def findAllPage(self, request):
        data = Province.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return paginator(request, data)
    
    def findById(self, id):
        data = Province.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
        return data.first()
    
    def save(self, data: Province):
        data.concat_values_fields()
        return data.save()
    
    def update(self, data: Province):
        data.concat_values_fields()
        Province.objects.filter(id = data.id).update(name = data.name, concat_fields = data.concat_fields)
        return data
    
    def remove(self, id):
        data = self.findById(id)
        Province.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    