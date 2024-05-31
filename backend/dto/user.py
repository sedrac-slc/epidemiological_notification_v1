from django.contrib.auth.models import User
from backend.entities.concrect.person import Person
from backend.entities.concrect.doctor import Doctor
from backend.utils.user import get_firstname, get_lastname

# Parse request for objects model
def user_request(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = get_lastname(request.POST.get('username'))
    last_name = get_lastname(request.POST.get('fullname'))
    first_name = get_firstname(request.POST.get('fullname'))
    data = User(
        username = username, 
        first_name = first_name, 
        last_name = last_name, 
        password = password , 
        email = email
    )
    return data

def person_request(request, user):
    person = Person(
        user = user,
        phone = request.POST.get('phone'),
        gender = request.POST.get('gender'),
        fullname = request.POST.get('fullname'),
        birthday = request.POST.get('birthday'),
        maritalStatus = request.POST.get('maritalStatus'),
        identityCardNumber = request.POST.get('identityCardNumber'),
    )
    return person

def doctor_request(request, person):
    doctor = Doctor(person = person)
    return doctor

# Persiste request in model
def create_user(request):
    user = user_request(request)
    user.save()
    return user

def create_person(request):
    user = create_user(request)
    person = person_request(request, user)
    person.concat_values_fields()
    person.save()
    return person

def create_doctor(request):
    person = create_person(request)
    doctor = doctor_request(request, person)
    doctor.concat_values_fields()
    doctor.save()
    return doctor
