#data, hora, sintomas
from django.db import models
from django.db.models import PROTECT
from backend.entity import EntityCommon
from .patient import Patient
from .doctor import Doctor
from .institution import Institution
from .payment_method import PaymentMethod
from .consultation_type import ConsultationType

class MedicalAppointment(EntityCommon):
    doctor = models.ForeignKey(Doctor, on_delete = PROTECT)    
    patient = models.ForeignKey(Patient, on_delete = PROTECT)
    institution = models.ForeignKey(Institution, on_delete = PROTECT)
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete = PROTECT)
    consultationType = models.ForeignKey(ConsultationType, on_delete = PROTECT)
    valuePay = models.BigIntegerField()
    data = models.DateField()
    hour = models.TimeField()
    description = models.TextField(max_length=255,null=True, blank=True)

    def concat_values_fields(self):
        super().concat_values_fields([self.description, self.data, self.hour, self.valuePay])