from backend.entities.concrect.province import Province
from backend.entities.concrect.municipal import Municipal

def to_municipal(request):
    province = Province(id = request.POST.get('province'))
    data = Municipal(name = request.POST.get('name'),  province = province)
    return data

def to_municipal_model(request):
    province = Province(id = request.POST.get('province'))
    data = Municipal(id = request.POST.get('model') , name = request.POST.get('name'), province = province)
    return data