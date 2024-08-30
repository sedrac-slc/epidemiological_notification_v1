from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from backend.service.concrect.sickness import SicknessService
from backend.dto.sickness import to_sickness, to_sickness_model

sicknessService = SicknessService()

# Create your views here.
@login_required
def index(request):
    data = sicknessService.findAllPage(request)
    return render(request, "pages/sickness.html", {
        'data': data, 
        'title': 'Doenças',
        'store': reverse('sickness.store'),
        'update': reverse('sickness.update'),
        'delete': reverse('sickness.delete') 
    })

@login_required
def store(request):
    if request.method != "POST": return redirect('sickness.index')
    sicknessService.save(to_sickness(request))
    messages.success(request, 'Doença cadastrada com successo!')
    return redirect('sickness.index')
   
@login_required
def update(request):
    if request.method != "POST": return redirect('sickness.index') 
    sicknessService.update(to_sickness_model(request))
    messages.success(request, 'Doença editada com successo!')
    return redirect('sickness.index')

@login_required
def delete(request):
    if request.method != "POST": return redirect('sickness.index')
    sicknessService.hidden(request.POST.get('model'))
    messages.success(request, 'Doença eliminada com successo!')
    return redirect('sickness.index')