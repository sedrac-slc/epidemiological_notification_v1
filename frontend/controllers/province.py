from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from backend.service.concrect.province import ProvinceService

service = ProvinceService()

# Create your views here.
def index(request):
    data = service.findAllPage(request)
    return render(request, "pages/province.html", {
        'data': data, 
        'title': 'Província',
        'store': reverse('province.store'),
        'update': reverse('province.update'),
        'delete': reverse('province.delete') 
    })

def store(request):
    if request.method == "GET": 
        return redirect('province.index')
    service.save(request)
    messages.success(request, 'Província cadastrada com successo!')
    return redirect('province.index')
   

def update(request):
    if request.method == "POST":
        
        messages.success(request, 'Ação concluída com sucesso!')
        return redirect('province.index')
    return redirect('province.index')

def delete(request):
    if request.method == "POST":
        
        messages.success(request, 'Ação concluída com sucesso!')
        return redirect('province.index')
    return redirect('province.index')