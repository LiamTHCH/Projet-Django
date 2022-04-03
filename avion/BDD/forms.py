from django import forms
from django.forms import ModelForm
from . import models
from django.utils.translation import gettext_lazy as _
class BA(ModelForm):
    class Meta:
        model = models.Base
        fields = ('nom', 'ville', 'num')
        labels = {
        'nom' : _('Nom de la base'),
        'ville' : _('Ville') ,
        'num' : _('Num')
        }