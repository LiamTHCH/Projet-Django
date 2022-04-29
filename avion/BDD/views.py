from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from . import models
from django.forms.models import model_to_dict
# Create your views here.
def index(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all() 
    avm =  models.AvionModele.objects.all()
    ttav = len(av)
    ttba = len(ba)
    ttes = len(es)
    ttavm = len(avm)
    return render(request, 'acc_av.html',{"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,"TTBA": ttba,"TTAV": ttav,"TTES": ttes,"TTAVM": ttavm})


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
            return HttpResponseRedirect('/show/av')
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


def show_av(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_av.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})


def show_av_id(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_av_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})


def update_es(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    instance = models.Escadron.objects.get(id=id)
    form = ES(instance=instance)
    if request.method == 'POST':
        form = ES(request.POST, instance=instance)
        if form.is_valid():
            form.save(commit=False)
            form.id = id # modification de l'id de l'objet
            print(form.id)
            form.save()
            return HttpResponseRedirect('/show/es')
    return render(request, 'es_update.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})


def update_ba(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    instance = models.Base.objects.get(id=id)
    form = BA(instance=instance)
    if request.method == 'POST':
        form = BA(request.POST, instance=instance)
        if form.is_valid():
            form.save(commit=False)
            form.id = id # modification de l'id de l'objet
            print(form.id)
            form.save()
            return HttpResponseRedirect('/show/ba')
    return render(request, 'ba_update.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})



def show_avm(request):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_avm.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})



def show_avm_id(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    return render(request, 'show_avm_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})


def update_avm(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    instance = models.AvionModele.objects.get(id=id)
    form = AVM(instance=instance)
    if request.method == 'POST':
        form = AVM(request.POST, instance=instance)
        if form.is_valid():
            form.save(commit=False)
            form.id = id # modification de l'id de l'objet
            print(form.id)
            form.save()
            return HttpResponseRedirect('/show/avm')
    return render(request, 'avm_update.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})



def del_av(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    instance = models.Avion.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/show/av')


def update_av(request,id):
    ba = models.Base.objects.all()
    es = models.Escadron.objects.all() 
    av = models.Avion.objects.all()
    avm =  models.AvionModele.objects.all()
    instance = models.Avion.objects.get(id=id)
    data = model_to_dict(instance)
    print(data["date_service"])
    print(data["date_service"].strftime("%Y-%m-%d"))
    data["date_service"] = data["date_service"].strftime("%Y-%m-%d")
    print(data)
    form = AV(initial=data)
    if request.method == 'POST':
        form = AV(request.POST,initial=data)
        if form.is_valid():
            temp = models.Avion(base=models.Base.objects.get(id=int(form.cleaned_data.get("base")[0])),code_avion=form.cleaned_data.get("code_avion"),escadron=models.Escadron.objects.get(id=int(form.cleaned_data.get("escadron")[0])),modele=models.AvionModele.objects.get(id=int(form.cleaned_data.get("modele")[0])),date_service=form.cleaned_data.get("date"))
            temp.id = id
            temp.save()
            return HttpResponseRedirect('/show/av')
    return render(request, 'av_update.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id,'date':data["date_service"]})