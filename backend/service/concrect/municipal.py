from backend.entities.concrect.municipal import Municipal
from backend.service.helper import paginator
from django.utils import timezone

class MunicipalService:

    def findAll(self, request):
        return Municipal.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        data = self.findAll(request)
        return paginator(request, data)
    
    def findById(self, id):
        data = Municipal.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
        return data.first()

    def findAllByProvince(self, id):
        data = Municipal.objects.filter(province = id, deleted_at__isnull=True, deleted_by__isnull=True)
        return data.all()
        
    def save(self, data: Municipal):
        data.concat_values_fields()
        return data.save()
    
    def update(self, data: Municipal):
        data.concat_values_fields()
        Municipal.objects.filter(id = data.id).update(name = data.name, province = data.province, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Municipal.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data  