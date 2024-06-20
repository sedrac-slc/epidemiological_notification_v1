
from backend.entities.concrect.institution import Institution
from .municipality import MunicipalityData
from enum import Enum

class InstitutionData(Enum):
    INSTITUTION_ONE = Institution(name="Hospital Geral de Benguela", group="público", director="José Tomás", location="Benguela, Quioxe" , municipality = MunicipalityData.BENGUELA.value)
    INSTITUTION_TWO = Institution(name="Hospital Geral de Luanda", group="público", director="Mária Lopez", location="Luanda, Camama", municipality = MunicipalityData.KILAMBA_KIAXI.value)
    INSTITUTION_THREE = Institution(name="Clínica Multiperfil", group="privado", director="Cardoso Afonso", location="Luanda, Morro Bento", municipality = MunicipalityData.SAMBA.value)
    INSTITUTION_FOUR = Institution(name="Clínica Katyvala", group="privado", director="Jorge Pena", location="Huambo, Matala", municipality = MunicipalityData.HUAMBO.value)
    
    ALL = [
       INSTITUTION_ONE, INSTITUTION_TWO, INSTITUTION_THREE, INSTITUTION_FOUR
    ]
 