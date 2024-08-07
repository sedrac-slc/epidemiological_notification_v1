from django.core.management.base import BaseCommand
from backend.utils.data import get_item_by_name, get_item_by_username, get_item_by_identity_card_number

from backend.service.concrect.laboratory_technician import LaboratoryTechnicianService
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.institution import InstitutionService
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.patient import PatientService
from backend.service.concrect.doctor import DoctorService
from backend.service.concrect.person import PersonService
from backend.service.concrect.group import GroupService
from backend.service.concrect.user import UserService
from backend.service.concrect.zone import ZoneService

from backend.data.laboratory_technician import LaboratoryTechnicianData
from backend.data.municipality import MunicipalityData
from backend.data.institution import InstitutionData
from backend.data.province import ProvinceData
from backend.data.sickness import SicknessData
from backend.data.patient import PatientData
from backend.data.doctor import DoctorData
from backend.data.person import PersonData
from backend.data.group import GroupData
from backend.data.user import UserData
from backend.data.zone import ZoneData

laboratoryTechnicianService = LaboratoryTechnicianService()
municipalityService = MunicipalityService()
institutionService = InstitutionService()
provinceService = ProvinceService()
sicknessService = SicknessService()
patientService = PatientService()
doctorService = DoctorService()
personService = PersonService()
groupService = GroupService()
userService = UserService()
zoneService = ZoneService()

class Command(BaseCommand):
    
    def handle(self, *args, **options):

        #users = UserData.ALL.value
        zones = ZoneData.ALL.value
        groups  = GroupData.ALL.value
        persons = PersonData.ALL.value
        #doctors = DoctorData.ALL.value
        #patienties = PatientData.ALL.value
        provinces  = ProvinceData.ALL.value
        sicknesies = SicknessData.ALL.value
        institutions = InstitutionData.ALL.value
        municipalities = MunicipalityData.ALL.value
        #laboratory_technicians = LaboratoryTechnicianData.ALL.value
        
        for group in groups:
            groupService.findOrSave(group)
            
        for zone in zones:
            zoneService.findOrSave(zone)            

        for province in provinces:
            province = provinceService.findOrSave(province)

        for sickness in sicknesies:
            sickness = sicknessService.findOrSave(sickness) 

        for municipality in municipalities:
            municipality.province = get_item_by_name(provinces, municipality.province)
            municipality = municipalityService.findOrSave(municipality)  

        for institution in institutions:
            institution.municipality = get_item_by_name(municipalities, institution.municipality)
            institution = institutionService.findOrSave(institution)

        for sickness in sicknesies:
            sickness = sicknessService.findOrSave(sickness)

        #for user in users:
        #    user = userService.findOrSave(user)
        
        #for person in persons:
        #    person.institution = get_item_by_name(institutions, person.institution)
        #    person = personService.findOrSave(person)
        
        #for doctor in doctors:
        #    doctor.person = personService.findByIdentityCardNumber(doctor.person)
        #    doctor = doctorService.findOrSave(doctor)
        
        #for patient in patienties:
        #    patient.person = personService.findByIdentityCardNumber(patient.person)
        #    patient = patientService.findOrSave(patient)
        
        #for laboratory_technician in laboratory_technicians:
        #    laboratory_technician.person = personService.findByIdentityCardNumber(laboratory_technician.person)
        #    laboratory_technician = laboratoryTechnicianService.findOrSave(laboratory_technician) 