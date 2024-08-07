from django.db import models
from backend.entity import EntityCommon

class Zone(EntityCommon):
    name = models.TextField(max_length=255)

    def concat_values_fields(self):
        super().concat_values_fields([self.name])    