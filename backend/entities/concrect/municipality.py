from django.db import models
from django.db.models import PROTECT
from backend.entity import EntityCommon
from .province import Province

class Municipality(EntityCommon):
    province = models.ForeignKey(Province, on_delete = PROTECT)
    name = models.TextField(max_length=255)

    def concat_values_fields(self):
        super().concat_values_fields([self.name])    