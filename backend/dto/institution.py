from backend.entities.concrect.municipal import Municipal
from backend.entities.concrect.institution import Institution

def to_institution(request):
    municipal = Municipal(id = request.POST.get('municipal'))
    data = Institution(name = request.POST.get('name'),  municipal = municipal)
    return data

def to_institution_model(request):
    municipal = Municipal(id = request.POST.get('municipal'))
    data = Institution(
        id = request.POST.get('model') , 
        name = request.POST.get('name'), 
        municipal = municipal
    )
    return data