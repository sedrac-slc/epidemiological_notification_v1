from backend.entities.concrect.person import Person
from backend.service.concrect.user import UserService
from django.contrib.auth.models import User
from django.db import transaction

userService = UserService()

class PersonService:
   
    def findByUser(self, user: User):
        return Person.objects.filter(user = user, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Person):
        try:
            with transaction.atomic():
                data.user = userService.findOrSave(data.user)
                return self.save(data)
        except Exception:
            return data
    
    def save(self, data: Person):
        data.save()
        return data