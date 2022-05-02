from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from . import models
from django.forms.models import model_to_dict
# Create your views here.
def index(request):
    ba = models.Base.objects.all() # queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all() # queryset pour le squellete
    avm =  models.AvionModele.objects.all() # queryset pour le squellete
    ttav = len(av) #compteur pour la page d'acceuil
    ttba = len(ba) #compteur pour la page d'acceuil
    ttes = len(es) #compteur pour la page d'acceuil
    ttavm = len(avm) #compteur pour la page d'acceuil
    return render(request, 'acc_av.html',{"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,"TTBA": ttba,"TTAV": ttav,"TTES": ttes,"TTAVM": ttavm}) #request avec toutes les infos


def ajout_ba(request):
    ba = models.Base.objects.all() # queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all() # queryset pour le squellete
    avm =  models.AvionModele.objects.all() # queryset pour le squellete
    if request.method == 'POST': #Recupere les info en POST
        form = BA(request.POST) #Recupere les info en POST
        if form.is_valid(): # test si le formulaire est valid
            form.save() # enregistre le formulaire
            return HttpResponseRedirect('/show/ba') #redirige vers la page de des bases
    else:
        form = BA() # si le formulaire n'est pas en POST
    return render(request, 'ba_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm}) #request avec toutes les infos et le formulaire




def ajout_es(request):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    if request.method == 'POST':#Recupere les info en POST
        form = ES(request.POST)#Recupere les info en POST
        if form.is_valid():# test si le formulaire est valid
            form.save()# enregistre le formulaire
            return HttpResponseRedirect('/')#redirige vers la page de des escadron
    else:
        form = ES()# si le formulaire n'est pas en POST
    return render(request, 'es_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})#request avec toutes les infos et le formulaire


def ajout_av(request):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all() # queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    if request.method == 'POST':#Recupere les info en POST
        form = AV(request.POST)#Recupere les info en POST
        if form.is_valid():# test si le formulaire est valid
           # print(int(form.cleaned_data.get("base")[0]))   #(debug)
           # print(models.Base.objects.get(id=int(form.cleaned_data.get("base")[0])))   #(debug)
           # print(form.cleaned_data.get("code_avion"))
           # print(models.Escadron.objects.get(id=int(form.cleaned_data.get("escadron")[0])))   #(debug)
           # print(models.AvionModele.objects.get(id=int(form.cleaned_data.get("modele")[0])))  #(debug)
           # print(form.cleaned_data.get("date")) #(debug)

           # recupere les infos du formulaire pour les enregistrer dans le modele (obliger de faire comme cela a cause du multiple choice fields)
            temp = models.Avion(base=models.Base.objects.get(id=int(form.cleaned_data.get("base")[0])),code_avion=form.cleaned_data.get("code_avion"),escadron=models.Escadron.objects.get(id=int(form.cleaned_data.get("escadron")[0])),modele=models.AvionModele.objects.get(id=int(form.cleaned_data.get("modele")[0])),date_service=form.cleaned_data.get("date"))
            temp.save()
            return HttpResponseRedirect('/show/av')
    else:
        form = AV()
    return render(request, 'av_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})


def ajout_avm(request):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    if request.method == 'POST':
        form = AVM(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AVM()
    return render(request, 'avm_ajout.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})



def show_ba(request):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_ba.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm}) #request avec toutes les infos et les info pour la page


def show_ba_id(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_ba_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id}) #request avec toutes les infos et le info pour la page (ID)



def del_ba(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    instance = models.Base.objects.get(id=id) #charge la bonne instance avec le bon ID
    instance.delete() #supprime l'instance
    return HttpResponseRedirect('/show/ba') #redirection



def show_es(request):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_es.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})#request avec toutes les infos et les info pour la page


def show_es_id(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_es_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})#request avec toutes les infos et le info pour la page (ID)


def del_es(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    instance = models.Escadron.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/show/es')


def show_av(request):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_av.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})


def show_av_id(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_av_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})


def update_es(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    instance = models.Escadron.objects.get(id=id) #charge la bonne instance avec le bon ID
    form = ES(instance=instance) #prerempli le formulaire
    if request.method == 'POST': #Recupere les info en POST
        form = ES(request.POST, instance=instance)#Recupere les info en POST et les infos prerempli
        if form.is_valid():
            form.save(commit=False)
            form.id = id # modification de l'id de l'objet
            #print(form.id)
            form.save()
            return HttpResponseRedirect('/show/es')
    return render(request, 'es_update.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})


def update_ba(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
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
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_avm.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm})



def show_avm_id(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    return render(request, 'show_avm_id.html', {"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id})


def update_avm(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
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
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    instance = models.Avion.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/show/av')


def update_av(request,id):
    ba = models.Base.objects.all()# queryset pour le squellete
    es = models.Escadron.objects.all() # queryset pour le squellete
    av = models.Avion.objects.all()# queryset pour le squellete
    avm =  models.AvionModele.objects.all()# queryset pour le squellete
    instance = models.Avion.objects.get(id=id)
    data = model_to_dict(instance)
    #print(data["date_service"]) #(debug)
    #print(data["date_service"].strftime("%Y-%m-%d"))#(debug)
    data["date_service"] = data["date_service"].strftime("%Y-%m-%d") #changement du format de date
    #print(data)
    form = AV(initial=data)
    if request.method == 'POST':
        form = AV(request.POST,initial=data)
        if form.is_valid():

            # recupere les infos du formulaire pour les enregistrer dans le modele (obliger de faire comme cela a cause du multiple choice fields)
            temp = models.Avion(base=models.Base.objects.get(id=int(form.cleaned_data.get("base")[0])),code_avion=form.cleaned_data.get("code_avion"),escadron=models.Escadron.objects.get(id=int(form.cleaned_data.get("escadron")[0])),modele=models.AvionModele.objects.get(id=int(form.cleaned_data.get("modele")[0])),date_service=form.cleaned_data.get("date"))
            temp.id = id
            temp.save()
            return HttpResponseRedirect('/show/av')
    return render(request, 'av_update.html', {'form': form,"BA" : ba,"ES" : es,"AV" : av,"AVM" : avm,'ID':id,'date':data["date_service"]}) #request avec toutes les infos et le formulaire plus injection de la date a cause du selecteur