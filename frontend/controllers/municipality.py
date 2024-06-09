from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from django.utils.html import escape
from backend.service.concrect.province import ProvinceService
from backend.service.concrect.municipality import MunicipalityService
from backend.dto.municipality import to_municipality , to_municipality_model

provinceService = ProvinceService()
municipalService = MunicipalityService()

# Create your views here.
def index(request):
    provinces = provinceService.findAll()
    data = municipalService.findAllPage(request)
    return render(request, "pages/municipality.html", { 
        'data': data, 
        'title': 'Município',
        'provinces': provinces,
        'store': reverse('municipality.store'),
        'update': reverse('municipality.update'),
        'delete': reverse('municipality.delete') 
    })
    
def store(request):
    if request.method != "POST": return redirect('municipal.index')
    municipalService.save(to_municipality(request))
    messages.success(request, 'Municipio cadastrada com successo!')
    return redirect('municipality.index')
   

def update(request):
    if request.method != "POST": return redirect('municipal.index') 
    municipalService.update(to_municipality_model(request))
    messages.success(request, 'Municipio editada com successo!')
    return redirect('municipality.index')

def delete(request):
    if request.method != "POST": return redirect('municipal.index')
    municipalService.hidden(request.POST.get('model'))
    messages.success(request, 'Municipio eliminada com successo!')
    return redirect('municipality.index')    

def province(request):
    municipals = []
    municipals = municipalService.findAllByProvince(request.GET.get('province'))
    data = ''.join([
        f'<option value="{escape(i.id)}" {"selected" if str(i.id) == request.GET.get('municipality') else ""}>{escape(i.name)}</option>'
        for i in municipals
    ])
    return HttpResponse(data, content_type="text/html;charset=utf-8")