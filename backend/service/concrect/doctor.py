from backend.entities.concrect.doctor import Doctor
from backend.entities.concrect.person import Person
from backend.service.concrect.person import PersonService
from backend.service.helper import paginator
from backend.dto.doctor import create_doctor, update_doctor, hidden_doctor, find_by_id
from backend.utils.data import save_model
from django.db import transaction

personService = PersonService()

class DoctorService:
   
    def findAll(self):
       return Doctor.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)   
    
    def findAllPage(self, request):
        return paginator(request, self.findAll())
    
    def findById(self, id):
        return find_by_id(id)
    
    def findByPerson(self, doctor: Doctor):
        return Doctor.objects.filter(person = doctor.person, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Doctor):
        doctor = self.findByPerson(data)        
        if doctor != None: 
            return doctor
        return save_model(data)            
    
    def save(self, request):
        return create_doctor(request)
    
    def update(self, request):
        return update_doctor(request)
    
    def hidden(self, request):
        return hidden_doctor(request)