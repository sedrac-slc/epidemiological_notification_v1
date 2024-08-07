from backend.entities.concrect.commune import Commune
from backend.service.concrect.municipality import MunicipalityService
from backend.service.helper import paginator
from django.utils import timezone

municipalityService = MunicipalityService()

class CommuneService:

    def list(self):
        return Commune.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return Commune.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return Commune.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()    

    def findAllByMunicipality(self, id):
        municipality = municipalityService.findById(id)
        return Commune.objects.filter(municipality = municipality, deleted_at__isnull=True, deleted_by__isnull=True).all()
    
    def findOrSave(self, data: Commune):
        commune = self.findByName(data.name)
        if commune != None: 
            return commune
        return self.save(data)    
        
    def save(self, data: Commune):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: Commune):
        data.concat_values_fields()
        Commune.objects.filter(id = data.id).update(name = data.name, municipality = data.municipality, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Commune.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data  