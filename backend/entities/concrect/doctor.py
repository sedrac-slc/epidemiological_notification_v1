from django.db import models
from backend.entity import EntityCommon
from.person import Person

class Doctor(EntityCommon):
    person = models.OneToOneField(Person, on_delete = models.CASCADE)
    
    def concat_values_fields(self):
        super().concat_values_fields([self.person.identityCardNumber, self.person.phone, self.person.gender, self.person.birthday])