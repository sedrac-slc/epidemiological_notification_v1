from backend.entities.concrect.person import Person
from backend.enums import FullnameEnum
from .institution import InstitutionData
from .user import UserData
from enum import Enum

def person_create(user, instituion, identityCardNumber, fullname, birthday, phone, gender, maritalStatus):
    return Person(
        user = user,
        phone = phone,
        gender = gender,
        fullname = fullname,
        birthday = birthday,
        maritalStatus = maritalStatus,
        institution = instituion,
        identityCardNumber = identityCardNumber,
    )

class PersonData(Enum):
    PAULO = person_create(UserData.PAULO.value,InstitutionData.INSTITUTION_ONE.value, "003023123LA001", FullnameEnum.PAULO.value, "1994-11-20","960123987","MALE","SINGLE")
    MARTA = person_create(UserData.MARTA.value,InstitutionData.INSTITUTION_TWO.value, "002045187BE025", FullnameEnum.MARTA.value, "1990-04-19","962423908","FEMALE","MARRIED")
    PEDRO = person_create(UserData.PEDRO.value,InstitutionData.INSTITUTION_THREE.value, "001045163LA059", FullnameEnum.PEDRO.value, "1985-09-07","962183280","MALE","MARRIED")
    
    BELA = person_create(UserData.BELA.value,InstitutionData.INSTITUTION_FOUR.value, "004926127BG023", FullnameEnum.BELA.value, "1987-01-11","961123907","FEMALE","SINGLE")
    FERNANDO = person_create(UserData.FERNANDO.value,InstitutionData.INSTITUTION_ONE.value, "005829143KS039", FullnameEnum.FERNANDO.value, "1997-05-02","965129979","MALE","MARRIED")
    HELENA = person_create(UserData.HELENA.value,InstitutionData.INSTITUTION_TWO.value, "006093720LA902", FullnameEnum.HELENA.value, "1994-10-28","966853986","FEMALE","SINGLE")
    
    RENATO = person_create(UserData.RENATO.value,InstitutionData.INSTITUTION_THREE.value, "007093123LA953", FullnameEnum.RENATO.value, "1994-11-20","967120997","MALE","SINGLE")
    ZAITA = person_create(UserData.ZAITA.value,InstitutionData.INSTITUTION_FOUR.value, "009020163LA682", FullnameEnum.ZAITA.value, "1969-11-20","968523357","FEMALE","WIDOWER")

    ALL = [PAULO, MARTA, PEDRO, BELA, FERNANDO, HELENA, RENATO, ZAITA]
