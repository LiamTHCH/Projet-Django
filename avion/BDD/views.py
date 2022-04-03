from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'main.html')


def ajout_ba(request):
    if request.method == 'POST':
        form = BA(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BA()
    return render(request, 'ba_ajout.html', {'form': form})