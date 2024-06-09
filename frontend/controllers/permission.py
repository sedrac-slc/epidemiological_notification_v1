from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from backend.service.concrect.permission import PermissionService
from backend.service.concrect.group import GroupService
from backend.parser.permission import createTablePlus

groupService = GroupService()
permissionService = PermissionService()

# Create your views here.
def index(request):
    data = permissionService.findAllPage(request)
    return render(request, "pages/permission.html", { 
        'data': data,
        'title': 'Permissões',
    })
    

def group_plus(request, id):
    permission = permissionService.findById(id)
    groups = groupService.findInId(request.POST.getlist('groups'))
    for group in groups:
        if not permission.group_set.filter(id=group.id).exists():
            permission.group_set.add(group)
    messages.success(request, 'Grupos adicionada ao grupo com successo!')
    return redirect('permission.index')

def group_list(request, id):
    permission = permissionService.findById(id)
    groups = groupService.findInId(request.POST.getlist('groups'))
    for group in groups:
        if permission.group_set.filter(id=group.id).exists():
            permission.group_set.remove(group)
    messages.success(request, 'Grupos removida ao grupo com successo!')
    return redirect('permission.index')

def plus(request, id):
    groups = groupService.findNotInPermission(id)
    data = createTablePlus(groups, "groups")
    return HttpResponse(data, content_type="text/html;charset=utf-8")
    
def lists(request,id):
    permission = permissionService.findById(id)
    groups = permission.group_set.all()
    data = createTablePlus(groups,"groups", "Eliminar")
    return HttpResponse(data, content_type="text/html;charset=utf-8")