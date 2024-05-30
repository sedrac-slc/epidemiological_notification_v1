from backend.entities.concrect.municipal import Municipal

def to_municipal(request):
    data = Municipal(name = request.POST.get('name') )
    return data

def to_municipal_model(request):
    data = Municipal(id = request.POST.get('model') , name = request.POST.get('name') )
    return data