from backend.entities.concrect.municipality import Municipality
from backend.entities.concrect.commune import Commune

def to_commune(request):
    municipality = Municipality(id = request.POST.get('municipality'))
    data = Commune(name = request.POST.get('name'),  municipality = municipality)
    return data

def to_commune_model(request):
    municipality = Municipality(id = request.POST.get('municipality'))
    data = Commune(id = request.POST.get('model') , name = request.POST.get('name'), municipality = municipality)
    return data