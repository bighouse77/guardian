from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return HttpResponse('LOGIN')

def home(request):
    return HttpResponse('HOME')

def glioma_analysis(request):
    return HttpResponse('GLIOMA ANALYSIS')

def blood_cell_analysis(request):
    return HttpResponse('BLOOD CELL ANALYSIS')