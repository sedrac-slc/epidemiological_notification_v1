from django.db import models
from django.db.models import PROTECT
from backend.entity import EntityCommon
from .laboratory_technician import LaboratoryTechnician
from .institution import Institution
from .patient import Patient
from .sickness import Sickness

def situations():
    return {
        'ALIVE': 'Vivo','DEAD': 'Morto','STABLE': 'Estável','CRITICAL': 'Crítico',
        'SEVERE': 'Grave','IMPROVING': 'Melhorando','RECOVERED': 'Recuperado','UNDER_OBSERVATION': 'Observação',
        'REFERRED': 'Referenciado','DISCHARGED': 'Alta','UNCONSCIOUS': 'Inconsciente','DECEASED': 'Falecido'
    }

def ratings():
    return {
        'CONFIRMED': 'Confirmado', 'SCHEDULED': 'Agendado', 'PENDING': 'Pendente', 'CANCELLED': 'Cancelado',
        'COMPLETED': 'Concluído', 'FAILED': 'Falhou', 'IN_PROGRESS': 'Em andamento', 'RESCHEDULED': 'Reagendado',
        'EXPIRED': 'Expirado', 'ON_HOLD': 'Em espera'
    }

class Notification(EntityCommon):
    institution = models.ForeignKey(Institution, on_delete = PROTECT)
    patient = models.ForeignKey(Patient, on_delete = PROTECT)
    laboratoryTechnician = models.ForeignKey(LaboratoryTechnician, on_delete = PROTECT)
    sickness = models.ForeignKey(Sickness, on_delete = PROTECT)
    observationDate = models.DateField()
    situation = models.CharField(choices= tuple((key, key) for key in situations()), max_length=100)
    manifestationDate = models.DateField()
    classification = models.CharField(choices= tuple((key, key) for key in ratings()), max_length=100)
    notificationDate = models.DateField()
    numberOfVaccines = models.IntegerField()
    vaccinationDate = models.DateField()
    
    class Meta:
        ordering = ['id']

    def concat_values_fields(self):
        super().concat_values_fields([ self.institution.name, self.patient.person.fullname, self.laboratoryTechnician.person.fullname])