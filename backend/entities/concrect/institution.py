from django.db import models
from backend.entity import EntityCommon

class Institution(EntityCommon):
    name = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    director = models.TextField(max_length=255)
    location = models.TextField(max_length=255)
    
    def concat_values_fields(self):
        super().concat_values_fields(f"{self.name},{self.type},{self.director},{self.location}")