
from backend.entities.concrect.province import Province
from enum import Enum

class ProvinceData(Enum):
    BENGO = Province(name="Bengo")
    BENGUELA = Province(name="Benguela")
    BIE = Province(name="Bié")
    CABINDA = Province(name="Cabinda")
    CUANDO_CUBANGO = Province(name="Cuando-Cubango")
    CUANZA_NORTE = Province(name="Cuanza Norte")
    CUANZA_SUL = Province(name="Cuanza Sul")
    CUNENE = Province(name="Cunene")
    HUAMBO = Province(name="Huambo")
    HUILA = Province(name="Huíla")
    LUANDA = Province(name="Luanda")
    LUNDA_NORTE = Province(name="Lunda Norte")
    LUNDA_SUL = Province(name="Lunda Sul")
    MALANJE = Province(name="Malanje")
    MOXICO = Province(name="Moxico")
    NAMIBE = Province(name="Namibe")
    UIGE = Province(name="Uíge")
    ZAIRE = Province(name="Zaire")
    
    ALL = [
        BENGO, BENGUELA, BIE, CABINDA, CUANDO_CUBANGO, CUANZA_NORTE, CUANZA_SUL, CUNENE,
        HUAMBO, HUILA, LUANDA, LUNDA_NORTE, LUNDA_SUL, MALANJE, MOXICO, NAMIBE, UIGE, ZAIRE
    ]
 