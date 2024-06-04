from backend.entities.concrect.doctor import Doctor
from django.utils import timezone
from .user import create_person, update_user, update_person, hidden_user, hidden_person

def find_by_id(id):
    data = Doctor.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
    return data.first()

def doctor_request(request, person):
    doctor = Doctor(person = person)
    return doctor

def create_doctor(request):
    person = create_person(request)
    doctor = doctor_request(request, person)
    doctor.concat_values_fields()
    doctor.save()
    return doctor

def update_doctor(request):
    id = request.POST.get('model')
    doctor = find_by_id(id)
    doctor.person.user = update_user(request, doctor.person.user)
    doctor.person = update_person(request, doctor.person)
    doctor.concat_values_fields()
    Doctor.objects.filter(id = id).update(
        concat_fields = doctor.concat_fields,  
        updated_at = timezone.now()
    )
    return doctor

def hidden_doctor(request):
    id = request.POST.get('model')
    doctor = find_by_id(id)
    hidden_user(doctor.person.user)
    hidden_person(doctor.person)
    Doctor.objects.filter(id = id).update(deleted_at = timezone.now())
    return doctor
