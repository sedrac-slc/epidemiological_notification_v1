from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.group import GroupService
from backend.dto.group import to_group, to_group_model

groupService = GroupService()

# Create your views here.
def index(request):
    data = groupService.findAllPage(request)
    return render(request, "pages/group.html", {
        'data': data, 
        'title': 'Cargos',
        'store': reverse('group.store'),
        'update': reverse('group.update'),
        'delete': reverse('group.delete') 
    })

def store(request):
    if request.method != "POST": return redirect('group.index')
    groupService.save(to_group(request))
    messages.success(request, 'Cargo cadastrada com successo!')
    return redirect('group.index')
   

def update(request):
    if request.method != "POST": return redirect('group.index') 
    groupService.update(to_group_model(request))
    messages.success(request, 'Cargo editada com successo!')
    return redirect('group.index')

def delete(request):
    if request.method != "POST": return redirect('group.index')
    groupService.delete(request.POST.get('model'))
    messages.success(request, 'Cargo eliminada com successo!')
    return redirect('group.index')