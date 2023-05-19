from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('busca/', views.search, name='busca'),
    path('detalhes/<int:id>', views.details, name='detalhes'),
]

