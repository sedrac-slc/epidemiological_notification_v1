from django.db import models
from django.db.models import PROTECT
from backend.entity import EntityCommon
from .municipality import Municipality

class Institution(EntityCommon):
    municipality = models.ForeignKey(Municipality, on_delete = PROTECT)
    name = models.TextField(max_length=255, unique=True)
    group = models.TextField(max_length=255)
    director = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    
    class Meta:
        ordering = ['id']

    def concat_values_fields(self):
        super().concat_values_fields([ self.name, self.group, self.director, self.location])