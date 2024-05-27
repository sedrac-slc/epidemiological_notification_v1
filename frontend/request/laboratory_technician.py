from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/laboratory-technician.html", { 'title': 'Técnico de laboratório'})