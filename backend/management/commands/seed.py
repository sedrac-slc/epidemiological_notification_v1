from django.core.management.base import BaseCommand
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.institution import InstitutionService
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.group import GroupService
from backend.data.municipality import MunicipalityData
from backend.data.institution import InstitutionData
from backend.data.province import ProvinceData
from backend.data.sickness import SicknessData
from backend.data.group import GroupData

municipalityService = MunicipalityService()
institutionService = InstitutionService()
provinceService = ProvinceService()
sicknessService = SicknessService()
groupService = GroupService()

class Command(BaseCommand):

    def handle(self, *args, **options):

        groups  = GroupData.ALL.value
        sicknesies = SicknessData.ALL.value
        institutions = InstitutionData.ALL.value

        for group in groups:
            groupService.findOrSave(group)

        for sicknes in sicknesies:
            sicknessService.findOrSave(sicknes) 

        for institution in institutions:
            institutionService.findOrSave(institution) 

        provinces  = ProvinceData.ALL.value
        for province in provinces:
            province = provinceService.findOrSave(province)
            for municipality in MunicipalityData.get(province):
                    municipalityService.findOrSave(municipality)
        
