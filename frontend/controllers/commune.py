from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.municipality import MunicipalityService
from backend.service.concrect.commune import CommuneService
from backend.dto.commune import to_commune , to_commune_model

communeService = CommuneService()
municipalityService = MunicipalityService()

# Create your views here.
def index(request):
    municipaties = municipalityService.findAll()
    data = communeService.findAllPage(request)
    return render(request, "pages/commune.html", { 
        'data': data, 
        'title': 'Comuna',
        'municipals': municipaties,
        'store': reverse('commune.store'),
        'update': reverse('commune.update'),
        'delete': reverse('commune.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('commune.index')
    communeService.save(to_commune(request))
    messages.success(request, 'Comuna cadastrada com successo!')
    return redirect('commune.index')
   
def update(request):
    if request.method != "POST": return redirect('commune.index') 
    communeService.update(to_commune_model(request))
    messages.success(request, 'Comuna editada com successo!')
    return redirect('commune.index')

def delete(request):
    if request.method != "POST": return redirect('commune.index')
    communeService.hidden(request.POST.get('model'))
    messages.success(request, 'Comuna eliminada com successo!')
    return redirect('commune.index')