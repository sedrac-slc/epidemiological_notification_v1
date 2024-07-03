from backend.entities.concrect.person import Person
from django.contrib.auth.models import User

class PersonService:
   
    def findByUser(self, user: User):
        return Person.objects.filter(user = user, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Person):
        person = self.findByUser(data.user)
        if person != None: 
            return person
        return self.save(data)
    
    def save(self, data: Person):
        data.save()
        return data