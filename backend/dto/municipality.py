from backend.entities.concrect.province import Province
from backend.entities.concrect.municipality import Municipality

def to_municipality(request):
    province = Province(id = request.POST.get('province'))
    data = Municipality(name = request.POST.get('name'),  province = province)
    return data

def to_municipality_model(request):
    province = Province(id = request.POST.get('province'))
    data = Municipality(id = request.POST.get('model') , name = request.POST.get('name'), province = province)
    return data