from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
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
    municipalService.hidden(request.POST.get('model'))
    messages.success(request, 'Municipio eliminada com successo!')
    return redirect('municipal.index')    

def province(request):
    municipals = []
    match request.method:
        case "GET":
            municipals = municipalService.findAllByProvince(request.GET.get('province'))
        case "POST":
            municipals = municipalService.findAllByProvince(request.POST.get('province'))
    data = ''.join([f'<option value="{i.id}">{i.name}</option>' for i in municipals])
    return JsonResponse(data, safe=False)