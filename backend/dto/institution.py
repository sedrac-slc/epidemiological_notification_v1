from backend.entities.concrect.municipality import Municipality
from backend.entities.concrect.institution import Institution

def to_institution(request):
    municipality = Municipality(id = request.POST.get('municipality'))
    data = Institution(
        name = request.POST.get('name'),
        group = request.POST.get('group'), 
        director = request.POST.get('director'),
        location = request.POST.get('location'),          
        municipality = municipality
    )
    return data

def to_institution_model(request):
    municipality = Municipality(id = request.POST.get('municipality'))
    data = Institution(
        id = request.POST.get('model'),
        name = request.POST.get('name'),  
        group = request.POST.get('group'), 
        director = request.POST.get('director'),
        location = request.POST.get('location'),
        municipality = municipality
    )
    return data