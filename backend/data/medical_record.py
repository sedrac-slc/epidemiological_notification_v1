from backend.entities.concrect.medical_record import MedicalRecord
from enum import Enum
from .sickness import SicknessData

class MedicalRecordData(Enum):
    COLERA = MedicalRecord(name="Ficha cólera", sickness = SicknessData.COLERA.value)
    MALARIA = MedicalRecord(name="Ficha malária", sickness = SicknessData.MALARIA.value)
    MENINGUITE = MedicalRecord(name="Ficha meninguite", sickness = SicknessData.MENINGUITE.value)
    FEBRE_TIFOIDE = MedicalRecord(name="Ficha febre Tifóide", sickness = SicknessData.FEBRE_TIFOIDE.value)
    FEBRE_AMARELA = MedicalRecord(name="Ficha febre Amarela", sickness = SicknessData.FEBRE_AMARELA.value)
    RAIVA_HUMANA = MedicalRecord(name="Ficha raiva Humana", sickness = SicknessData.RAIVA_HUMANA.value)
    OBITO_CRIANCA = MedicalRecord(name="Ficha óbito da criança", sickness = SicknessData.OBITO_CRIANCA.value)
    REACCAO_ADVERSA = MedicalRecord(name="Ficha reacções Adversas", sickness = SicknessData.REACCAO_ADVERSA.value)
    
    ALL = [
       COLERA, MALARIA, MENINGUITE, FEBRE_TIFOIDE, FEBRE_AMARELA, RAIVA_HUMANA, OBITO_CRIANCA, REACCAO_ADVERSA
    ]
 