from backend.entities.concrect.consultation_type import ConsultationType

def to_consultation_type(request):
    return ConsultationType(name = request.POST.get('name'), price = request.POST.get('price') )
    
def to_consultation_type_model(request):
    return ConsultationType(id = request.POST.get('model') , name = request.POST.get('name'), price = request.POST.get('price'))
    