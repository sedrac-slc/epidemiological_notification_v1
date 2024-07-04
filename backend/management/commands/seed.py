from django.core.management.base import BaseCommand
from backend.utils.data import get_item_by_name, get_item_by_identity_card_number

from backend.service.concrect.laboratory_technician import LaboratoryTechnicianService
from backend.service.concrect.consultation_type import ConsultationTypeService
from backend.service.concrect.medical_record import MedicalRecordService
from backend.service.concrect.payment_method import PaymentMethodService
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.institution import InstitutionService
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.patient import PatientService
from backend.service.concrect.doctor import DoctorService
from backend.service.concrect.person import PersonService
from backend.service.concrect.group import GroupService
from backend.service.concrect.user import UserService

from backend.data.laboratory_technician import LaboratoryTechnicianData
from backend.data.consultation_type import ConsultationTypeData
from backend.data.medical_record import MedicalRecordData
from backend.data.payment_method import PaymentMethodData
from backend.data.municipality import MunicipalityData
from backend.data.institution import InstitutionData
from backend.data.province import ProvinceData
from backend.data.sickness import SicknessData
from backend.data.patient import PatientData
from backend.data.doctor import DoctorData
from backend.data.person import PersonData
from backend.data.group import GroupData
from backend.data.user import UserData

consultationTypeService = ConsultationTypeService()
medicalRecordService = MedicalRecordService()
paymentMethodService = PaymentMethodService()
municipalityService = MunicipalityService()
institutionService = InstitutionService()
provinceService = ProvinceService()
sicknessService = SicknessService()
patientService = PatientService()
doctorService = DoctorService()
personService = PersonService()
groupService = GroupService()
userService = UserService()

class Command(BaseCommand):
    
    def handle(self, *args, **options):

        #users = UserData.ALL.value
        groups  = GroupData.ALL.value
        persons = PersonData.ALL.value
        doctors = DoctorData.ALL.value
        patienties = PatientData.ALL.value
        provinces  = ProvinceData.ALL.value
        sicknesies = SicknessData.ALL.value
        institutions = InstitutionData.ALL.value
        municipalities = MunicipalityData.ALL.value
        medical_records = MedicalRecordData.ALL.value
        payment_methods = PaymentMethodData.ALL.value
        consultation_types = ConsultationTypeData.ALL.value
        
        for group in groups:
            groupService.findOrSave(group)

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

        for medical_record in medical_records:
            medical_record.sickness = get_item_by_name(sicknesies, medical_record.sickness)
            medical_record = medicalRecordService.findOrSave(medical_record)

        for consultation_type in consultation_types:
            consultation_type = consultationTypeService.findOrSave(consultation_type)
            
        for payment_method in payment_methods:
            payment_method = paymentMethodService.findOrSave(payment_method)
        
        for person in persons:
            person.institution = get_item_by_name(institutions, person.institution)
            person = personService.findOrSave(person)
        
        #for doctor in doctors:
            #doctor.person = get_item_by_identity_card_number(persons, doctor.person)
            #doctor = doctorService.findOrSave(doctor)
