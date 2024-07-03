
from backend.entities.concrect.consultation_type import ConsultationType
from enum import Enum

class ConsultationTypeData(Enum):
    NORMAL = ConsultationType(name="Normal", price= 3500)
    FASTER = ConsultationType(name="Rápido", price= 5000)
    
    ALL = [
        NORMAL, FASTER
    ]
 