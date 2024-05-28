from django.db import models
from backend.entity import EntityCommon

class Province(EntityCommon):
    name = models.TextField(max_length=255, unique=True)
    def concat_values_fields(self):
        super().concat_values_fields([self.name])    