from django.db import models
from django.db.models import PROTECT
from backend.entity import EntityCommon
from backend.enums import CONTACT_TYPES
from .patient import Patient


class Contact(EntityCommon):
    patient = models.ForeignKey(Patient, on_delete = PROTECT)
    number = models.TextField(max_length=255)
    type = models.CharField(choices= CONTACT_TYPES, max_length=100)

    def concat_values_fields(self):
        super().concat_values_fields([self.name, self.type])    