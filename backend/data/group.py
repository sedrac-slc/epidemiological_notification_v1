
from django.contrib.auth.models import Group
from enum import Enum

class GroupData(Enum):
    
    DOCTOR = Group(name="Médicos")
    PATIENT = Group(name="Pacientes")
    LABORATORY_TECHNICIAN = Group(name="Técnicos de Laboratórios")
    
    ALL = [DOCTOR, PATIENT, LABORATORY_TECHNICIAN]
 