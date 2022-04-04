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
           # print(int(form.cleaned_data.get("base")[0]))
           # print(models.Base.objects.get(id=int(form.cleaned_data.get("base")[0])))
           # print(form.cleaned_data.get("code_avion"))
           # print(models.Escadron.objects.get(id=int(form.cleaned_data.get("escadron")[0])))
           # print(models.AvionModele.objects.get(id=int(form.cleaned_data.get("modele")[0])))
           # print(form.cleaned_data.get("date"))
            temp = models.Avion(base=models.Base.objects.get(id=int(form.cleaned_data.get("base")[0])),code_avion=form.cleaned_data.get("code_avion"),escadron=models.Escadron.objects.get(id=int(form.cleaned_data.get("escadron")[0])),modele=models.AvionModele.objects.get(id=int(form.cleaned_data.get("modele")[0])),date_service=form.cleaned_data.get("date"))
            temp.save()
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



def show_ba(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_ba.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})



def show_ba_id(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_ba_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})



def del_ba(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    instance = models.Base.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/show/ba')



def show_es(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_es.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})


def show_es_id(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_es_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})


def del_es(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    instance = models.Escadron.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/show/es')