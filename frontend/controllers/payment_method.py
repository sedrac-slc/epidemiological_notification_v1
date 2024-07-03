from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from backend.service.concrect.payment_method import PaymentMethodService
from backend.dto.payment_method import to_payment_method, to_payment_method_model

paymentMethodService = PaymentMethodService()

# Create your views here.
def index(request):
    data = paymentMethodService.findAllPage(request)
    return render(request, "pages/payment-method.html", {
        'data': data, 
        'title': 'Forma pagamento',
        'store': reverse('payment_method.store'),
        'update': reverse('payment_method.update'),
        'delete': reverse('payment_method.delete') 
    })

def store(request):
    if request.method != "POST": return redirect('payment_method.index')
    paymentMethodService.save(to_payment_method(request))
    messages.success(request, 'Forma pagamento cadastrada com successo!')
    return redirect('payment_method.index')
   

def update(request):
    if request.method != "POST": return redirect('payment_method.index') 
    paymentMethodService.update(to_payment_method_model(request))
    messages.success(request, 'Forma pagamento editada com successo!')
    return redirect('payment_method.index')

def delete(request):
    if request.method != "POST": return redirect('payment_method.index')
    paymentMethodService.hidden(request.POST.get('model'))
    messages.success(request, 'Forma pagamento eliminada com successo!')
    return redirect('payment_method.index')