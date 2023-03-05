from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)

from users.views import deleteuser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('vereinsapp/', views.index, name='index'),
    path('angebote/', views.angebote, name='angebote'),
    #path('angebotsprofil/', views.angebotsprofil),
    path('vereinsmarketing/', views.vereinsmarketing, name='vereinsmarketing'),
    path('anzeige_new/', views.anzeige_new),
    path('nutzerprofil/', views.nutzerprofil, name='Nprofile'),
    path('filter/', views.filter_list, name='filter'),

    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', views.anzeige_new, name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
