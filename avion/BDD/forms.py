from django import forms
from django.forms import ModelForm
from . import models
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import NumberInput

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

class AV(forms.Form): #pas modlesForm a cause du multiplechoice fields
    modele = forms.MultipleChoiceField(choices=[(c.id,c.nom) for c in models.AvionModele.objects.all()])
    code_avion = forms.CharField()
    escadron = forms.MultipleChoiceField(choices=[(c.id, str(c.nom)) for c in models.Escadron.objects.all()])
    base = forms.MultipleChoiceField(choices=[(c.id, str(c.nom+" "+str(c.num))) for c in models.Base.objects.all()])
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date','id':'datepick'}))
    

