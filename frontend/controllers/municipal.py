from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.municipal import MunicipalService
from backend.dto.municipal import to_municipal , to_municipal_model

service = MunicipalService()

# Create your views here.
def index(request):
    data = service.findAllPage(request)
    return render(request, "pages/municipal.html", { 
        'data': data, 
        'title': 'Município',
        'store': reverse('municipal.store'),
        'update': reverse('municipal.update'),
        'delete': reverse('municipal.delete')         
    })
    
def store(request):
    if request.method != "POST": return redirect('municipal.index')
    
    service.save(to_municipal(request))
    messages.success(request, 'Municipio cadastrada com successo!')
    return redirect('municipal.index')
   

def update(request):
    if request.method != "POST": return redirect('municipal.index') 
    
    service.update(to_municipal_model(request))
    messages.success(request, 'Municipio editada com successo!')
    return redirect('municipal.index')

def delete(request):
    if request.method != "POST": return redirect('municipal.index')
    
    service.remove(request.POST.get('model'))
    messages.success(request, 'Municipio eliminada com successo!')
    return redirect('municipal.index')    