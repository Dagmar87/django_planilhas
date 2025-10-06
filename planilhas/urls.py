from django.urls import path
from . import views

urlpatterns = [
    path('importar/', views.importar_planilha, name='importar_planilha'),
]