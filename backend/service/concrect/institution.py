from django.utils import timezone
from backend.entities.concrect.institution import Institution
from backend.service.helper import paginator

class InstitutionService:
    
    def findAllPage(self, request):
        data = Institution.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return paginator(request, data)
    
    def findById(self, id):
        return Institution.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def save(self, data: Institution):
        data.concat_values_fields()
        return data.save()
    
    def update(self, data: Institution):
        data.concat_values_fields()
        Institution.objects.filter(id = data.id).update(
            name = data.name, 
            group = data.group,
            director = data.director,
            location = data.location,
            municipality = data.municipality,
            concat_fields = data.concat_fields
        )
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Institution.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data       