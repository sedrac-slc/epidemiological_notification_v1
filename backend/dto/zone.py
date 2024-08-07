from backend.entities.concrect.zone import Zone

def to_zone(request):
    return Zone(name = request.POST.get('name') )
    
def to_zone_model(request):
    data = to_zone(request)
    data.id = request.POST.get('model')
    return data