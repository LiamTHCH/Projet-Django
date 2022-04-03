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

class ES(ModelForm):
    class Meta:
        model = models.Escadron
        fields = ('nom',)
        labels = {
        'nom' : _("Nom de l'escadron")
        }



class AVM(ModelForm):
    class Meta:
        model = models.AvionModele
        fields = ('nom',)
        labels = {
        'nom' : _("Nom du modéle")
        }

class AV(forms.Form):
    modele = forms.MultipleChoiceField(choices=[(c.id,c.nom) for c in models.AvionModele.objects.all()])
    code_avion = forms.CharField()
    escadron = forms.MultipleChoiceField(choices=[(c.id, str(c.nom)) for c in models.Escadron.objects.all()])
    base = forms.MultipleChoiceField(choices=[(c.id, str(c.nom+" "+str(c.num))) for c in models.Base.objects.all()])
    date = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    

