from backend.entities.concrect.municipality import Municipality
from backend.entities.concrect.institution import Institution

def to_institution(request):
    municipal = Municipality(id = request.POST.get('municipal'))
    data = Institution(name = request.POST.get('name'),  municipal = municipal)
    return data

def to_institution_model(request):
    municipal = Municipality(id = request.POST.get('municipal'))
    data = Institution(
        id = request.POST.get('model') , 
        name = request.POST.get('name'), 
        municipal = municipal
    )
    return data