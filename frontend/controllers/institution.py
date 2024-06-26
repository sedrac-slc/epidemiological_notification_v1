from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.institution import InstitutionService
from backend.dto.institution import to_institution , to_institution_model

provinceService = ProvinceService()
institutionService = InstitutionService()
# Create your views here.
def index(request):
    provinces = provinceService.findAll()
    data = institutionService.findAllPage(request)
    return render(request, "pages/institution.html", { 
        'data': data, 
        'title': 'Instituição',
        'provinces': provinces,
        'store': reverse('institution.store'),
        'update': reverse('institution.update'),
        'delete': reverse('institution.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('institution.index')
    institutionService.save(to_institution(request))
    messages.success(request, 'Instituição cadastrada com successo!')
    return redirect('institution.index')
   

def update(request):
    if request.method != "POST": return redirect('institution.index') 
    institutionService.update(to_institution_model(request))
    messages.success(request, 'Instituição editada com successo!')
    return redirect('institution.index')

def delete(request):
    if request.method != "POST": return redirect('institution.index')
    institutionService.hidden(request.POST.get('model'))
    messages.success(request, 'Instituição eliminada com successo!')
    return redirect('institution.index')    