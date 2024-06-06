from django.core.management.base import BaseCommand
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.province import ProvinceService
from backend.data.municipality import MunicipalityData
from backend.data.province import ProvinceData

provinceService = ProvinceService()
municipalityService = MunicipalityService()

class Command(BaseCommand):

    def handle(self, *args, **options):
        provinces  = ProvinceData.ALL.value
        for province in provinces:
            province = provinceService.findOrSave(province)
            for municipality in MunicipalityData.get(province):
                    municipalityService.findOrSave(municipality)
        
