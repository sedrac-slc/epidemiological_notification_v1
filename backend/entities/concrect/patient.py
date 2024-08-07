from django.db import models
from backend.entity import EntityCommon
from.person import Person

class Patient(EntityCommon):
    person = models.OneToOneField(Person, on_delete = models.CASCADE)
    phoneTwo = models.TextField(max_length=255,null=True, blank=True)
    residence = models.TextField(max_length=255, null=True, blank=True)
    neighborhood = models.TextField(max_length=255, null=True, blank=True)
    referencePoint = models.TextField(max_length=255, null=True, blank=True)
    fullnameFather = models.TextField(max_length=255, null=True, blank=True)
    fullnameMother = models.TextField(max_length=255, null=True, blank=True)
    
    def concat_values_fields(self):
        super().concat_values_fields([
            self.person.fullname, 
            self.person.identityCardNumber, 
            self.person.phone, 
            self.person.gender,
            self.person.maritalStatus, 
            self.person.birthday,
        ])