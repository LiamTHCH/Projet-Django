from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from . import models
# Create your views here.
def index(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all() 
    avm =  models.AvionModele.objects.all()
    return render(request, 'main.html',{"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})


def ajout_ba(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all() 
    avm =  models.AvionModele.objects.all()
    if request.method == 'POST':
        form = BA(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BA()
    return render(request, 'ba_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})




def ajout_es(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all() 
    avm =  models.AvionModele.objects.all()
    if request.method == 'POST':
        form = ES(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ES()
    return render(request, 'es_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})


def ajout_av(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all() 
    avm =  models.AvionModele.objects.all()
    if request.method == 'POST':
        form = AV(request.POST)
        if form.is_valid():
            temp = form.cleaned_data.get("base")
            print(temp)
            return HttpResponseRedirect('/')
    else:
        form = AV()
    return render(request, 'av_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})


def ajout_avm(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    if request.method == 'POST':
        form = AVM(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AVM()
    return render(request, 'avm_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})