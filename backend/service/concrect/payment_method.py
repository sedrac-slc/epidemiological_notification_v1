from backend.entities.concrect.payment_method import PaymentMethod
from backend.service.helper import paginator
from django.utils import timezone

class PaymentMethodService:
   
    def findAll(self):
        return PaymentMethod.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
    
    def findAllPage(self, request):
        return paginator(request, self.findAll())
    
    def findById(self, id):
        return PaymentMethod.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByName(self, name):
        return PaymentMethod.objects.filter(name = name, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: PaymentMethod):
        paymentMethod = self.findByName(data.name)
        if paymentMethod != None: 
            return paymentMethod
        return self.save(data)
    
    def save(self, data: PaymentMethod):
        data.concat_values_fields()
        data.save()
        return data
    
    def update(self, data: PaymentMethod):
        data.concat_values_fields()
        PaymentMethod.objects.filter(id = data.id).update(name = data.name, concat_fields = data.concat_fields)
        return data
    
    def hidden(self, id):
        data = self.findById(id)
        PaymentMethod.objects.filter(id = data.id).update(deleted_at = timezone.now())
        return data    