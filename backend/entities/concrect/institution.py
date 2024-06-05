from django.db import models
from django.db.models import PROTECT
from backend.entity import EntityCommon
from .municipality import Municipality

class Institution(EntityCommon):
    municipality = models.OneToOneField(Municipality, on_delete = PROTECT)
    name = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    director = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    
    def concat_values_fields(self):
        super().concat_values_fields([ self.name, self.type, self.director, self.location])