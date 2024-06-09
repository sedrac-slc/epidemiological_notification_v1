from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from backend.service.concrect.permission import PermissionService
from backend.service.concrect.group import GroupService
from backend.dto.group import to_group, to_group_model
from backend.parser.permission import createTablePlus

groupService = GroupService()
permissionService = PermissionService()

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

def permission_plus(request, id):
    group = groupService.findById(id)
    permissions = permissionService.findInId(request.POST.getlist('permissions'))
    for permission in permissions:
        if not group.permissions.filter(id=permission.id).exists():
            group.permissions.add(permission)
    messages.success(request, 'Permissões adicionada ao grupo com successo!')
    return redirect('group.index')

def permission_list(request, id):
    group = groupService.findById(id)
    permissions = permissionService.findInId(request.POST.getlist('permissions'))
    for permission in permissions:
        if group.permissions.filter(id=permission.id).exists():
            group.permissions.remove(permission)
    messages.success(request, 'Permissões removida ao grupo com successo!')
    return redirect('group.index')

def plus(request, id):
    #id de Group fazer um consultar para pegar exculir a permissiões que pertence ao grupo
    permissions = permissionService.findNotInGroup(id)
    data = createTablePlus(permissions, "permissions")
    return HttpResponse(data, content_type="text/html;charset=utf-8")
    
def lists(request,id):
    group = groupService.findById(id)
    permissions = group.permissions.all()
    data = createTablePlus(permissions,"permissions", "Eliminar")
    return HttpResponse(data, content_type="text/html;charset=utf-8")
