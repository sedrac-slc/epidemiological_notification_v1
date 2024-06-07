from django.shortcuts import render
from backend.service.concrect.permission import PermissionService

permissionService = PermissionService()

# Create your views here.
def index(request):
    data = permissionService.findAllPage(request)
    return render(request, "pages/permission.html", { 
        'data': data,
        'title': 'Permissões',
    })