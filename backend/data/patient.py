
from backend.entities.concrect.patient import Patient
from .person import PersonData
from enum import Enum

def user_patient(person):
    return Patient(person = person)

class PatientData(Enum):
    BELA = user_patient(PersonData.BELA.value)
    FERNANDO = user_patient(PersonData.FERNANDO.value)
    HELENA = user_patient(PersonData.HELENA.value)
    
    ALL = [BELA, FERNANDO, HELENA]