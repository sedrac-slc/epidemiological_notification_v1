from backend.entities.concrect.sickness import Sickness

def to_sickness(request):
    data = Sickness(name = request.POST.get('name') )
    return data

def to_sickness_model(request):
    data = Sickness(id = request.POST.get('model') , name = request.POST.get('name') )
    return data