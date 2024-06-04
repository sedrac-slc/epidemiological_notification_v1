from backend.entities.concrect.laboratory_technician import LaboratoryTechnician
from django.utils import timezone
from .user import create_person, update_user, update_person, hidden_user, hidden_person

def find_by_id(id):
    data = LaboratoryTechnician.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
    return data.first()

def laboratory_technician_request(request, person):
    laboratory_technician = LaboratoryTechnician(person = person)
    return laboratory_technician

def create_laboratory_technician(request):
    person = create_person(request)
    laboratory_technician = laboratory_technician_request(request, person)
    laboratory_technician.concat_values_fields()
    laboratory_technician.save()
    return laboratory_technician

def update_laboratory_technician(request):
    id = request.POST.get('model')
    laboratory_technician = find_by_id(id)
    laboratory_technician.person.user = update_user(request, laboratory_technician.person.user)
    laboratory_technician.person = update_person(request, laboratory_technician.person)
    laboratory_technician.concat_values_fields()
    LaboratoryTechnician.objects.filter(id = id).update(
        concat_fields = laboratory_technician.concat_fields,  
        updated_at = timezone.now()
    )
    return laboratory_technician

def hidden_laboratory_technician(request):
    id = request.POST.get('model')
    laboratory_technician = find_by_id(id)
    hidden_user(laboratory_technician.person.user)
    hidden_person(laboratory_technician.person)
    LaboratoryTechnician.objects.filter(id = id).update(deleted_at = timezone.now())
    return laboratory_technician
