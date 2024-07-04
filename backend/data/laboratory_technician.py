
from backend.entities.concrect.laboratory_technician import LaboratoryTechnician
from .person import PersonData
from enum import Enum

def user_laboratory_technician(person):
    return LaboratoryTechnician(person = person)

class LaboratoryTechnicianData(Enum):
    RENATO = user_laboratory_technician(PersonData.RENATO.value)
    ZAITA = user_laboratory_technician(PersonData.ZAITA.value)
    
    ALL = [RENATO, ZAITA]