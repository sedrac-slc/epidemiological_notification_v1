from django.contrib.auth.models import User
from backend.entities.concrect.person import Person
from backend.utils.user import get_firstname, get_lastname

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

def person_request(request, user = None):
    person = Person(
        phone = request.POST.get('phone'),
        gender = request.POST.get('gender'),
        fullname = request.POST.get('fullname'),
        birthday = request.POST.get('birthday'),
        maritalStatus = request.POST.get('maritalStatus'),
        identityCardNumber = request.POST.get('identityCardNumber'),
    )
    if user:
        person.user = user
    return person