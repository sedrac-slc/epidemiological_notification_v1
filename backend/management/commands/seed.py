from django.core.management.base import BaseCommand
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.group import GroupService
from backend.data.municipality import MunicipalityData
from backend.data.province import ProvinceData
from backend.data.sickness import SicknessData
from backend.data.group import GroupData

municipalityService = MunicipalityService()
provinceService = ProvinceService()
sicknessService = SicknessService()
groupService = GroupService()

class Command(BaseCommand):

    def handle(self, *args, **options):
        groups  = GroupData.ALL.value
        sicknesies = SicknessData.ALL.value

        for sicknes in sicknesies:
            sicknessService.findOrSave(sicknes) 

        for group in groups:
            group = groupService.findOrSave(group)

        provinces  = ProvinceData.ALL.value
        for province in provinces:
            province = provinceService.findOrSave(province)
            for municipality in MunicipalityData.get(province):
                    municipalityService.findOrSave(municipality)
        
