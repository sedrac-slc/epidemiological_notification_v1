from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from backend.service.concrect.province import ProvinceService
from backend.dto.province import to_province, to_province_model

service = ProvinceService()

# Create your views here.
def index(request):
    data = service.findAllPage(request)
    return render(request, "pages/province.html", {
        'data': data, 
        'title': 'Província',
        'store': reverse('province.store'),
        'update': reverse('province.update'),
        'delete': reverse('province.delete') 
    })

def store(request):
    if request.method != "POST": return redirect('province.index')
    
    service.save(to_province(request))
    messages.success(request, 'Província cadastrada com successo!')
    return redirect('province.index')
   

def update(request):
    if request.method != "POST": return redirect('province.index') 
    
    service.update(to_province_model(request))
    messages.success(request, 'Província editada com successo!')
    return redirect('province.index')

def delete(request):
    if request.method != "POST": return redirect('province.index')
    
    service.remove(request.POST.get('model'))
    messages.success(request, 'Província eliminada com successo!')
    return redirect('province.index')