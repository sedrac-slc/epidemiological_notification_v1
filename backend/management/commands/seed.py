from django.core.management.base import BaseCommand
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.group import GroupService
from backend.data.municipality import MunicipalityData
from backend.data.province import ProvinceData
from backend.data.group import GroupData

municipalityService = MunicipalityService()
provinceService = ProvinceService()
groupService = GroupService()

class Command(BaseCommand):

    def handle(self, *args, **options):
        groups  = GroupData.ALL.value
        
        for group in groups:
            group = groupService.findOrSave(group)

        provinces  = ProvinceData.ALL.value
        for province in provinces:
            province = provinceService.findOrSave(province)
            for municipality in MunicipalityData.get(province):
                    municipalityService.findOrSave(municipality)
        
