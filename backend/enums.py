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

CONTACT_TYPES = [
    ('PRINCIPAL', 'PRINCIPAL'),
    ('ALTERNATIVE', 'ALTERNATIVE'),
    ('WHATSAPP', 'WHATSAPP'),
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