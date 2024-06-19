from backend.entities.concrect.medical_record import MedicalRecord
from backend.service.concrect.sickness import SicknessService
from backend.service.helper import paginator
from django.utils import timezone

sicknessService = SicknessService()

class MedicalRecordService:

    def list(self):
        return MedicalRecord.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return MedicalRecord.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return MedicalRecord.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()    

    def findAllBySickness(self, id):
        province = sicknessService.findById(id)
        return MedicalRecord.objects.filter(province = province, deleted_at__isnull=True, deleted_by__isnull=True).all()
    
    def findOrSave(self, data: MedicalRecord):
        municipality = self.findByName(data.name)
        if municipality != None: 
            return municipality
        return self.save(data)    
        
    def save(self, data: MedicalRecord):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: MedicalRecord):
        data.concat_values_fields()
        MedicalRecord.objects.filter(id = data.id).update(name = data.name, sickness = data.sickness, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        MedicalRecord.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data  