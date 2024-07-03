from backend.entities.concrect.province import Province

def to_province(request):
    return Province(name = request.POST.get('name') )
    
def to_province_model(request):
    data = to_province(request)
    data.id = request.POST.get('model')
    return data