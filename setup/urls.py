from django.contrib import admin
from django.urls import path, include
from oficina.views import carViewSet, clienteViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', carViewSet.get),
    path('cars/post', carViewSet.post),
    path('cars/delete', carViewSet.delete),
    path('cars/put', carViewSet.put),
    path('clientes/', clienteViewSet.get),
    path('clientes/post', clienteViewSet.post),
    path('clientes/delete', clienteViewSet.delete),
    path('clientes/put', clienteViewSet.put),
]
