from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'guardian/pages/login/login.html')

def home(request):
    return render(request, 'guardian/pages/home.html')

def glioma_analysis(request):
    return render(request, 'guardian/pages/glioma/glioma_analysis.html')

def patients(request):
    return render(request, 'guardian/pages/patients/patients.html')

def register_patients(request):
    return render(request, 'guardian/pages/register_patients/register_patients.html')

def about(request):
    return render(request, 'guardian/pages/about/about.html')

def contact(request):
    return render(request, 'guardian/pages/contact/contact.html')

def blood_cell_analysis(request):
    return render(request, 'guardian/home.html')
