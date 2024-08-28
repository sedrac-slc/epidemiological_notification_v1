from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.institution import InstitutionService
from backend.service.concrect.notification import NotificationService
from backend.dto.notification import to_notification, to_notification_model
from backend.entities.concrect.notification import situations, ratings

sicknessService = SicknessService()
institutionService = InstitutionService()
notificationService = NotificationService()

# Create your views here.
def index(request):
    data = notificationService.findAll()
    sicknesies = sicknessService.findAll()
    institutions = institutionService.findAll()
    return render(request, "pages/notification.html", {
        'data': data, 
        'institutions': institutions,
        'sicknesies': sicknesies,
        'situations': situations,
        'ratings': ratings,
        'title': 'Notificação',
        'store': reverse('notification.store'),
        'update': reverse('notification.update'),
        'delete': reverse('notification.delete') 
    })

def store(request):
    if request.method != "POST": return redirect('notification.index')
    notificationService.save(to_notification(request))
    messages.success(request, 'Notificação cadastrada com successo!')
    return redirect('notification.index')

def update(request):
    if request.method != "POST": return redirect('notification.index') 
    notificationService.update(to_notification_model(request))
    messages.success(request, 'Notificação editada com successo!')
    return redirect('notification.index')

def delete(request):
    if request.method != "POST": return redirect('notification.index')
    notificationService.hidden(request.POST.get('model'))
    messages.success(request, 'Notificação eliminada com successo!')
    return redirect('notification.index')