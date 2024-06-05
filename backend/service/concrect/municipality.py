from backend.entities.concrect.municipality import Municipality
from backend.service.concrect.province import ProvinceService
from backend.service.helper import paginator
from django.utils import timezone

provinceService = ProvinceService()

class MunicipalityService:

    def findAll(self, request):
        return Municipality.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        data = self.findAll(request)
        return paginator(request, data)
    
    def findById(self, id):
        data = Municipality.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
        return data.first()

    def findAllByProvince(self, id):
        province = provinceService.findById(id)
        data = Municipality.objects.filter(province = province, deleted_at__isnull=True, deleted_by__isnull=True)
        return data.all()
        
    def save(self, data: Municipality):
        data.concat_values_fields()
        return data.save()
    
    def update(self, data: Municipality):
        data.concat_values_fields()
        Municipality.objects.filter(id = data.id).update(name = data.name, province = data.province, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Municipality.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data  