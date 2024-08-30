from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from backend.service.concrect.sickness import SicknessService
from backend.service.concrect.institution import InstitutionService
from backend.service.concrect.notification import NotificationService
from backend.dto.notification import to_notification, to_notification_model
from backend.entities.concrect.notification import situations, ratings

sicknessService = SicknessService()
institutionService = InstitutionService()
notificationService = NotificationService()

# Create your views here.
@login_required
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

@login_required
def store(request):
    if request.method != "POST": return redirect('notification.index')
    notificationService.save(to_notification(request))
    messages.success(request, 'Notificação cadastrada com successo!')
    return redirect('notification.index')

@login_required
def update(request):
    if request.method != "POST": return redirect('notification.index') 
    notificationService.update(to_notification_model(request))
    messages.success(request, 'Notificação editada com successo!')
    return redirect('notification.index')

@login_required
def delete(request):
    if request.method != "POST": return redirect('notification.index')
    notificationService.hidden(request.POST.get('model'))
    messages.success(request, 'Notificação eliminada com successo!')
    return redirect('notification.index')