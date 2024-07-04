from backend.entities.concrect.doctor import Doctor
from backend.entities.concrect.person import Person
from backend.service.helper import paginator
from backend.dto.doctor import create_doctor, update_doctor, hidden_doctor, find_by_id
from backend.utils.data import save_model

class DoctorService:
   
    def findAll(self):
       return Doctor.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)   
    
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return find_by_id(id)
    
    def findByPerson(self, person: Person):
        return Doctor.objects.filter(person = person, deleted_at__isnull=True, deleted_by__isnull=True).first()
    
    def findOrSave(self, data: Doctor):
        person = self.findByPerson(data.person)
        if person != None:
            return person
        return save_model(data)
    
    def save(self, request):
        return create_doctor(request)
    
    def update(self, request):
        return update_doctor(request)
    
    def hidden(self, request):
        return hidden_doctor(request)