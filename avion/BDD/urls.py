from django.urls import path
from . import views
urlpatterns = [
path('', views.index),
path('ajouter/ba', views.ajout_ba),
path('ajouter/es', views.ajout_es),
path('ajouter/av', views.ajout_av),
]