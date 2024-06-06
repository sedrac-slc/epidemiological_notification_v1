from django.db import models
from django.utils import timezone
import uuid

class EntityCommon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.UUIDField(null=True, blank=True)

    updated_at = models.DateTimeField(default=timezone.now)
    updated_by = models.UUIDField(null=True, blank=True)

    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.UUIDField(null=True, blank=True)

    concat_fields = models.TextField(unique=True)
    
    class Meta:
        abstract = True

    def getId(self):
        return self.id

    def concat_values_fields(self, parm):
        concatenated_parm = ";".join(parm)
        self.concat_fields = f"{self.id};{concatenated_parm};{self.created_at};{self.updated_at}"