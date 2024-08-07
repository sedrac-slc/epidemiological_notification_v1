from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.zone import ZoneService
from backend.dto.zone import to_zone, to_zone_model

zoneService = ZoneService()

# Create your views here.
def index(request):
    data = zoneService.findAllPage(request)
    return render(request, "pages/zone.html", {
        'data': data, 
        'title': 'Zona',
        'store': reverse('zone.store'),
        'update': reverse('zone.update'),
        'delete': reverse('zone.delete') 
    })

def store(request):
    if request.method != "POST": return redirect('zone.index')
    zoneService.save(to_zone(request))
    messages.success(request, 'Zona cadastrada com successo!')
    return redirect('zone.index')
   

def update(request):
    if request.method != "POST": return redirect('zone.index') 
    zoneService.update(to_zone_model(request))
    messages.success(request, 'Zona editada com successo!')
    return redirect('zone.index')

def delete(request):
    if request.method != "POST": return redirect('zone.index')
    zoneService.hidden(request.POST.get('model'))
    messages.success(request, 'Zona eliminada com successo!')
    return redirect('zone.index')