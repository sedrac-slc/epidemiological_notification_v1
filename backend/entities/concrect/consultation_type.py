#data, hora, sintomas
from django.db import models
from backend.entity import EntityCommon

class ConsultationType(EntityCommon):
    name = models.TextField(max_length=255, unique=True)
    price = models.BigIntegerField()
    
    def concat_values_fields(self):
        super().concat_values_fields([self.name]) 