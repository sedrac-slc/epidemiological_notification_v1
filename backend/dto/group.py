from django.contrib.auth.models import Group

def to_group(request):
    data = Group(name = request.POST.get('name'))
    return data

def to_group_model(request):
    data = Group(id = request.POST.get('model') , name = request.POST.get('name') )
    return data