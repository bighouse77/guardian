from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('glioma_analysis/', views.glioma_analysis),
    path('blood_cell_analysis', views.blood_cell_analysis)
]
