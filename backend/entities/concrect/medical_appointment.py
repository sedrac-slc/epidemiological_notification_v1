#data, hora, sintomas
from django.db import models
from django.db.models import PROTECT
from backend.entity import EntityCommon
from .patient import Patient
from .doctor import Doctor
from .consultation_type import ConsultationType

class MedicalAppointment(EntityCommon):
    patient = models.ForeignKey(Patient, on_delete = PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete = PROTECT)
    consultationType = models.ForeignKey(ConsultationType, on_delete = PROTECT)
    data = models.DateField()
    hour = models.TimeField()
    description = models.TextField(max_length=255)

    def concat_values_fields(self):
        super().concat_values_fields([self.description, self.accomplished])