from backend.entities.concrect.patient import Patient
from django.utils import timezone
from .user import create_person_patient, update_user, update_person, hidden_user, hidden_person

def find_by_id(id):
    data = Patient.objects.filter(id = id, deleted_at__isnull=True, deleted_by__isnull=True)
    return data.first()

def patient_request(request, person):
    patient = Patient(
        person = person,
        phoneTwo = request.POST.get('phoneTwo'),
        residence = request.POST.get('residence'),
        neighborhood = request.POST.get('neighborhood'),
        referencePoint = request.POST.get('referencePoint'),
        fullnameFather = request.POST.get('fullnameFather'),
        fullnameMother = request.POST.get('fullnameMother'),
    )
    return patient

def create_patient(request):
    person = create_person_patient(request)
    patient = patient_request(request, person)
    patient.concat_values_fields()
    patient.save()
    return patient

def update_patient(request):
    id = request.POST.get('model')
    patient = find_by_id(id)
    patient.person.user = update_user(request, patient.person.user)
    patient.person = update_person(request, patient.person)
    patient.concat_values_fields()
    Patient.objects.filter(id = id).update(
        phoneTwo = request.POST.get('phoneTwo'),
        residence = request.POST.get('residence'),
        neighborhood = request.POST.get('neighborhood'),
        referencePoint = request.POST.get('referencePoint'),
        fullnameFather = request.POST.get('fullnameFather'),
        fullnameMother = request.POST.get('fullnameMother'),        
        concat_fields = patient.concat_fields,  
        updated_at = timezone.now()
    )
    return patient

def hidden_patient(request):
    id = request.POST.get('model')
    patient = find_by_id(id)
    hidden_user(patient.person.user)
    hidden_person(patient.person)
    Patient.objects.filter(id = id).update(deleted_at = timezone.now())
    return patient
