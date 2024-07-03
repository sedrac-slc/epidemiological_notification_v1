from backend.entities.concrect.payment_method import PaymentMethod

def to_payment_method(request):
    return PaymentMethod(name = request.POST.get('name') )

def to_payment_method_model(request):
    return PaymentMethod(id = request.POST.get('model') , name = request.POST.get('name') )