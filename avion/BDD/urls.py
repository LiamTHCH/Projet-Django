from django.urls import path
from . import views
urlpatterns = [
path('', views.index),
path('ajouter/ba', views.ajout_ba),
path('ajouter/es', views.ajout_es),
path('ajouter/av', views.ajout_av),
path('ajouter/avm', views.ajout_avm),
path('show/ba', views.show_ba),
path('show/ba/<int:id>',views.show_ba_id),
path('del/ba/<int:id>',views.del_ba)
]