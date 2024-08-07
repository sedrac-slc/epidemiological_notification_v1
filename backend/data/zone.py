
from backend.entities.concrect.zone import Zone
from enum import Enum

class ZoneData(Enum):
    ZONA_A = Zone(name="Zona A")
    ZONA_E = Zone(name="Zona E")
    ZONA_I = Zone(name="Zona I")
    ZONA_O = Zone(name="Zona O")
    ZONA_U = Zone(name="Zona U")
   
    
    ALL = [
        ZONA_A, ZONA_E, ZONA_I, ZONA_O, ZONA_U,
    ]
 