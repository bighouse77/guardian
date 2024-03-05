from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'guardian/login/login.html')

def home(request):
    return render(request, 'guardian/pages/home.html')

def glioma_analysis(request):
    return render(request, 'guardian/glioma/glioma_analysis.html')

def blood_cell_analysis(request):
    return render(request, 'guardian/home.html')