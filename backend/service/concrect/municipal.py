from backend.entities.concrect.municipal import Municipal
from backend.service.helper import paginator
from django.utils import timezone

class MunicipalService:
    
    def findAllPage(self, request):
        data = Municipal.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return paginator(request, data)
    
    def findById(self, id):
        data = Municipal.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
        return data.first()
    
    def save(self, data: Municipal):
        data.concat_values_fields()
        return data.save()
    
    def update(self, data: Municipal):
        data.concat_values_fields()
        Municipal.objects.filter(id = data.id).update(name = data.name, concat_fields = data.concat_fields)
        return data
    
    def remove(self, id):
        data = self.findById(id)
        Municipal.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    