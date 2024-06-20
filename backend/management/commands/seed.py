from django.core.management.base import BaseCommand

from backend.service.concrect.medical_record import MedicalRecordService
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.institution import InstitutionService
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.group import GroupService

from backend.data.medical_record import MedicalRecordData
from backend.data.municipality import MunicipalityData
from backend.data.institution import InstitutionData
from backend.data.province import ProvinceData
from backend.data.sickness import SicknessData
from backend.data.group import GroupData

medicalRecordService = MedicalRecordService()
municipalityService = MunicipalityService()
institutionService = InstitutionService()
provinceService = ProvinceService()
sicknessService = SicknessService()
groupService = GroupService()

class Command(BaseCommand):

    def getSickness(self, sicknesies, sick):
        for sickness in sicknesies:
            if sickness.name == sick.name:
                return sickness
        return sick

    def getProvince(self, provinces, prov):
        for province in provinces:
            if province.name == prov.name:
                return province
        return prov

    def getMunicipality(self, municipalities, muni):
        for municipality in municipalities:
            if municipality.name == muni.name:
                return municipality
        return muni

    def handle(self, *args, **options):

        groups  = GroupData.ALL.value
        provinces  = ProvinceData.ALL.value
        sicknesies = SicknessData.ALL.value
        institutions = InstitutionData.ALL.value
        municipalities = MunicipalityData.ALL.value
        medical_records = MedicalRecordData.ALL.value
        
        for group in groups:
            groupService.findOrSave(group)

        for province in provinces:
            province = provinceService.findOrSave(province)

        for sickness in sicknesies:
            sickness = sicknessService.findOrSave(sickness) 

        for municipality in municipalities:
            municipality.province = self.getProvince(provinces, municipality.province)
            municipality = municipalityService.findOrSave(municipality)  

        for institution in institutions:
            institution.municipality = self.getMunicipality(municipalities, institution.municipality)
            institutionService.findOrSave(institution)

        for medical_record in medical_records:
            medical_record.sickness = self.getSickness(sicknesies, medical_record.sickness)
            medicalRecordService.findOrSave(medical_record)
        
