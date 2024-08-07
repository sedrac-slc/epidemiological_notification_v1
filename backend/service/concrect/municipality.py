from backend.entities.concrect.municipality import Municipality
from backend.service.concrect.province import ProvinceService
from backend.service.helper import paginator
from django.utils import timezone

provinceService = ProvinceService()

class MunicipalityService:

    def list(self):
        return Municipality.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
    
    def findAll(self):
        return self.list().all()
        
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return Municipality.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return Municipality.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()    

    def findAllByProvince(self, id):
        province = provinceService.findById(id)
        return Municipality.objects.filter(province = province, deleted_at__isnull=True, deleted_by__isnull=True).all()
    
    def findOrSave(self, data: Municipality):
        municipality = self.findByName(data.name)
        if municipality != None: 
            return municipality
        return self.save(data)    
        
    def save(self, data: Municipality):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: Municipality):
        data.concat_values_fields()
        Municipality.objects.filter(id = data.id).update(name = data.name, province = data.province, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Municipality.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data  