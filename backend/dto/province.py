from backend.entities.concrect.province import Province

def to_province(request):
    data = Province(name = request.POST.get('name') )
    return data

def to_province_model(request):
    data = Province(id = request.POST.get('model') , name = request.POST.get('name') )
    return data