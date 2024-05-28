from backend.entities.concrect.province import Province
from backend.service.helper import paginator

class ProvinceService:
    
    def findAllPage(self, request):
        data = Province.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return paginator(request, data)
    
    def save(self, request):
        data = Province(name = request.POST.get('name') )
        data.concat_values_fields()
        return data.save()