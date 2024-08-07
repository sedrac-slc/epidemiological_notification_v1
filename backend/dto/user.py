from django.contrib.auth.models import User
from django.utils import timezone
from backend.entities.concrect.person import Person
from backend.entities.concrect.institution import Institution
from backend.utils.user import get_firstname, get_lastname
from nanoid import generate

# Parse request for objects model
def user_request(request, passwordGenerator = False):
    
    if passwordGenerator:
        password = generate(size=10)
        username = "patient#".join(password)
        email =  f"p{password}@gmail.com"
    else:
        password = request.POST.get('password')
        username = request.POST.get('username')
        email = request.POST.get('email')
        
    last_name = get_lastname(request.POST.get('fullname'))
    first_name = get_firstname(request.POST.get('fullname'))
    return User(
        email = email,
        password = password, 
        username = username, 
        last_name = last_name, 
        first_name = first_name 
    )

def person_request(request, user):
    return Person(
        user = user,
        phone = request.POST.get('phone'),
        gender = request.POST.get('gender'),
        fullname = request.POST.get('fullname'),
        birthday = request.POST.get('birthday'),
        maritalStatus = request.POST.get('maritalStatus'),
        institution = Institution(request.POST.get('institution')),
        identityCardNumber = request.POST.get('identityCardNumber'),
    )

# Create object request in model
def create_user(request, passwordGenerator = False):
    user = user_request(request, passwordGenerator)
    user.save()
    return user

def create_person(request):
    user = create_user(request)
    person = person_request(request, user)
    person.concat_values_fields()
    person.save()
    return person

def create_person_patient(request):
    user = create_user(request,True)
    person = person_request(request, user)
    person.concat_values_fields()
    person.save()
    return person

# Update object request in model
def update_user(request, model): 
    user = user_request(request)
    User.objects.filter(id = model.id).update(
        last_name = user.last_name, 
        first_name = user.first_name,
    )
    return user    

def update_person(request, model): 
    person = person_request(request, model.user)
    person.concat_values_fields()
    Person.objects.filter(id = model.id).update(
        phone = person.phone,
        gender = person.gender,
        fullname = person.fullname,
        birthday = person.birthday,
        maritalStatus = person.maritalStatus,
        identityCardNumber = person.identityCardNumber,
        concat_fields = person.concat_fields,  
        deleted_at = timezone.now()
    )
    return person

# Hidden object request in model
def hidden_user(model): 
    User.objects.filter(id = model.id).update(is_active = False)
    return model 

def hidden_person(model):
    Person.objects.filter(id = model.id).update(deleted_at = timezone.now())
    return model     