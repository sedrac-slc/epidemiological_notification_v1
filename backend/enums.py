from enum import Enum

GENDER_CHOICES = [
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
]

MARITAL_STATUS_CHOICES = [
    ('SINGLE', 'SINGLE'),
    ('MARRIED', 'MARRIED'),
    ('WIDOWER', 'WIDOWER'),
    ('DIVORCED', 'DIVORCED'),
]

class FullnameEnum(Enum):
    PAULO = "Paulo Oliveira Santos"
    MARTA = "Marta Kina Velma"
    PEDRO = "Pedro Kahuma"
    BELA = "Bela José"
    FERNANDO = "Fernando Deliona Tchuma"
    HELENA = "Helena Pinha Duval"
    RENATO = "Renato Renal"
    ZAITA = "Zaita Lucas Nehima"