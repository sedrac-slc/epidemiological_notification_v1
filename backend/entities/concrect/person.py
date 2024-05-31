from django.db import models
from django.contrib.auth.models import User
from backend.entity import EntityCommon
from backend.enums import GENDER_CHOICES, MARITAL_STATUS_CHOICES

def genders():
    return {'MALE': 'Masculino', 'FEMALE': 'Feminino'}

def maritalStatus():
    return {'SINGLE': 'Solteiro', 'MARRIED': 'Casado(a)','WIDOWER': 'Viúvo(a)', 'DIVORCED': 'Divorciado(a)'}

# Create your models here.
class Person(EntityCommon):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.TextField(max_length=100)
    identityCardNumber = models.TextField(max_length=100, unique= True)
    phone = models.TextField(max_length=100, null=True, blank=True)
    gender = models.CharField(choices= GENDER_CHOICES, max_length=100)
    maritalStatus = models.CharField(choices= MARITAL_STATUS_CHOICES, max_length=100)
    birthday = models.DateField()

    def concat_values_fields(self):
        super().concat_values_fields([self.fullname, self.user.username, self.user.email, self.identityCardNumber, self.phone, self.gender, self.maritalStatus, self.birthday])  