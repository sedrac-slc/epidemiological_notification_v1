
from backend.entities.concrect.sickness import Sickness
from enum import Enum

class SicknessData(Enum):
    COLERA = Sickness(name="Colera")
    MALARIA = Sickness(name="Malária")
    MENINGUITE = Sickness(name="Meninguite")
    FEBRE_TIFOIDE = Sickness(name="Febre Tifóide")
    FEBRE_AMARELA = Sickness(name="Febre Amarela")
    RAIVA_HUMANA = Sickness(name="Raiva Humana")
    OBITO_CRIANCA = Sickness(name="Obito da criança")
    REACCAO_ADVERSA = Sickness(name="Reacções Adversas a medicamenentos e produtos sanitátios")
    
    ALL = [
       COLERA, MALARIA, MENINGUITE, FEBRE_TIFOIDE, FEBRE_AMARELA, RAIVA_HUMANA, OBITO_CRIANCA, REACCAO_ADVERSA
    ]
 