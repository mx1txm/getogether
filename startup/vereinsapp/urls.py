from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vereinsapp/', views.index, name='index'),
    path('angebote/', views.angebote),
    path('angebotsprofil/', views.angebotsprofil),
    path('vereinsmarketing/', views.vereinsmarketing),
    path('anzeige_new/', views.anzeige_new),
    path('nutzerprofil/', views.nutzerprofil),
]