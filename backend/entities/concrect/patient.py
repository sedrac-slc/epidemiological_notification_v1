from django.db import models
from backend.entity import EntityCommon
from.person import Person

class Patient(EntityCommon):
    person = models.OneToOneField(Person, on_delete = models.CASCADE)
    neighborhood = models.TextField(max_length=255)
    
    def concat_values_fields(self):
        super().concat_values_fields([
            self.person.fullname, 
            self.person.identityCardNumber, 
            self.person.phone, 
            self.person.gender,
            self.person.maritalStatus, 
            self.person.birthday,
        ])