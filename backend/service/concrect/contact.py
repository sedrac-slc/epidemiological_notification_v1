from backend.entities.concrect.contact import Contact
from backend.service.helper import paginator
from django.utils import timezone

class ContactService:
   
    def findAll(self):
        return Contact.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        
    def findAllPage(self, request):
        return paginator(request, self.findAll())
    
    def findById(self, id):
        return Contact.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByNumber(self, number):
        return Contact.objects.filter(number = number, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Contact):
        number = self.findByNumber(data.number)
        if number != None: 
            return number
        return self.save(data)
    
    def save(self, data: Contact):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: Contact):
        data.concat_values_fields()
        Contact.objects.filter(id = data.id).update(number = data.number, type = data.type, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        Contact.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    