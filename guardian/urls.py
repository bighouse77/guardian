from django.urls import path
from guardian.views import home, login, glioma_analysis, blood_cell_analysis

urlpatterns = [
    path('', home),
    path('login/', login),
    path('glioma_analysis/', glioma_analysis),
    path('blood_cell_analysis', blood_cell_analysis)
]
