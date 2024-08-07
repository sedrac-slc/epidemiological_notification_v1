from backend.entities.concrect.person import Person
from backend.service.concrect.user import UserService
from django.contrib.auth.models import User
from django.db import transaction

userService = UserService()

class PersonService:
   
    def findByUser(self, user: User):
        return Person.objects.filter(user = user, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findByIdentityCardNumber(self, person: Person):
        return Person.objects.filter(identityCardNumber = person.identityCardNumber, deleted_at__isnull=True, deleted_by__isnull=True).first()    
    
    def findOrSave(self, data: Person):
        person = self.findByIdentityCardNumber(data)        
        if person != None: 
            return person
        return self.save(data)
    
    def save(self, data: Person):
        data.concat_values_fields()
        data.save()
        return data