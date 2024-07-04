
from backend.entities.concrect.doctor import Doctor
from .person import PersonData
from enum import Enum

def user_doctor(person):
    return Doctor(person = person)

class DoctorData(Enum):
    PAULO = user_doctor(PersonData.PAULO.value)
    MARTA = user_doctor(PersonData.MARTA.value)
    PEDRO = user_doctor(PersonData.PEDRO.value)
    
    ALL = [PAULO, MARTA, PEDRO]