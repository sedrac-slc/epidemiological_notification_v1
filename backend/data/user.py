
from django.contrib.auth.models import User
from backend.utils.user import get_firstname, get_lastname
from backend.enums import FullnameEnum
from enum import Enum

def user_create(fullname,username,email,password="123456780a"):
    return User(
        email = email,
        password = password, 
        username = username, 
        last_name = get_lastname(fullname), 
        first_name = get_firstname(fullname) 
    )

class UserData(Enum):
    PAULO = user_create(FullnameEnum.PAULO.value,"paulo-santo","paulo.santos@system.ao")
    MARTA = user_create(FullnameEnum.MARTA.value,"marta-velma","marta.velma@system.ao")
    PEDRO = user_create(FullnameEnum.PEDRO.value,"pedro-kahuma","pedro.kahuma@system.ao")
    
    BELA = user_create(FullnameEnum.BELA.value,"bela-jose","bela.jose@system.ao")
    FERNANDO = user_create(FullnameEnum.FERNANDO.value,"fernando-tchuma","fernado.tchuma@system.ao")
    HELENA = user_create(FullnameEnum.HELENA.value,"helena-duval","helena.duval@system.ao")
    
    RENATO = user_create(FullnameEnum.RENATO.value,"renato-renal","renato.renal@system.ao")
    ZAITA = user_create(FullnameEnum.ZAITA.value,"zaita-nehima","zaita.nehima@system.ao")
    
    ALL = [
        PAULO, MARTA, PEDRO, BELA, FERNANDO, HELENA, RENATO, ZAITA
    ]
 