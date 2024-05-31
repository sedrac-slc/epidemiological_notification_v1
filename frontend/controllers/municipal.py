from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.municipal import MunicipalService
from backend.dto.municipal import to_municipal , to_municipal_model

provinceService = ProvinceService()
municipalService = MunicipalService()

# Create your views here.
def index(request):
    provinces = provinceService.findAll()
    data = municipalService.findAllPage(request)
    return render(request, "pages/municipal.html", { 
        'data': data, 
        'title': 'Município',
        'provinces': provinces,
        'store': reverse('municipal.store'),
        'update': reverse('municipal.update'),
        'delete': reverse('municipal.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('municipal.index')
    
    municipalService.save(to_municipal(request))
    messages.success(request, 'Municipio cadastrada com successo!')
    return redirect('municipal.index')
   

def update(request):
    if request.method != "POST": return redirect('municipal.index') 
    
    municipalService.update(to_municipal_model(request))
    messages.success(request, 'Municipio editada com successo!')
    return redirect('municipal.index')

def delete(request):
    if request.method != "POST": return redirect('municipal.index')
    
    municipalService.remove(request.POST.get('model'))
    messages.success(request, 'Municipio eliminada com successo!')
    return redirect('municipal.index')    