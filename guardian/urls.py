from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('glioma_analysis/', views.glioma_analysis, name='glioma_analysis'),
    path('blood_cell_analysis/', views.blood_cell_analysis, name='blood_cell_analysis'),
    path('patients/', views.patients, name='patients'),
    path('sobre/', views.about, name='about'),
    path('registrar/', views.register_patients, name='register_patients'),
    path('contact/', views.contact, name='contact'),
]
