from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.zone import ZoneService
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.institution import InstitutionService
from backend.dto.zone import to_zone, to_zone_model

zoneService = ZoneService()
sicknessService = SicknessService()
institutionService = InstitutionService()

def situations():
    return {
        'ALIVE': 'Vivo','DEAD': 'Morto','STABLE': 'Estável','CRITICAL': 'Crítico',
        'SEVERE': 'Grave','IMPROVING': 'Melhorando','RECOVERED': 'Recuperado','UNDER_OBSERVATION': 'Observação',
        'REFERRED': 'Referenciado','DISCHARGED': 'Alta','UNCONSCIOUS': 'Inconsciente','DECEASED': 'Falecido'
    }

def ratings():
    return {
        'CONFIRMED': 'Confirmado', 'SCHEDULED': 'Agendado', 'PENDING': 'Pendente', 'CANCELLED': 'Cancelado',
        'COMPLETED': 'Concluído', 'FAILED': 'Falhou', 'IN_PROGRESS': 'Em andamento', 'RESCHEDULED': 'Reagendado',
        'EXPIRED': 'Expirado', 'ON_HOLD': 'Em espera'
    }

# Create your views here.
def index(request):
    data = []
    sicknesies = sicknessService.findAll()
    institutions = institutionService.findAll()
    return render(request, "pages/notification.html", {
        'data': data, 
        'institutions': institutions,
        'sicknesies': sicknesies,
        'situations': situations,
        'ratings': ratings,
        'title': 'Notificação',
        'store': '#',
        'update': '#',
        'delete': '#' 
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