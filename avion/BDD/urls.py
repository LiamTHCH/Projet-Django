from django.urls import path
from . import views
urlpatterns = [
path('', views.index), #racine
path('ajouter/ba', views.ajout_ba),
path('ajouter/es', views.ajout_es),
path('ajouter/av', views.ajout_av),
path('ajouter/avm', views.ajout_avm),
path('show/ba', views.show_ba),
path('show/ba/<int:id>',views.show_ba_id),
path('del/ba/<int:id>',views.del_ba),
path('show/es', views.show_es),
path('show/es/<int:id>',views.show_es_id),
path('del/es/<int:id>',views.del_es),
path('show/av', views.show_av),
path('show/av/<int:id>',views.show_av_id),
path('up/es/<int:id>',views.update_es),
path('up/ba/<int:id>',views.update_ba),
path('show/avm', views.show_avm),
path('show/avm/<int:id>',views.show_avm_id),
path('up/avm/<int:id>',views.update_avm),
path('del/av/<int:id>',views.del_av),
path('up/av/<int:id>',views.update_av)
]