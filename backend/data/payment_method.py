from backend.entities.concrect.payment_method import PaymentMethod
from enum import Enum

class PaymentMethodData(Enum):
    MULTICAIXA = PaymentMethod(name="Multicaixa")
    CAIXA = PaymentMethod(name="Caixa")
    
    ALL = [
        MULTICAIXA, CAIXA,
    ]
 