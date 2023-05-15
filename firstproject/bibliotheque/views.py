from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LivreForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            livre = form.save()
            return render(request,"bibliotheque/affiche.html",{"livre" : livre})
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = LivreForm()
        return render(request,"bibliotheque/ajout.html",{"form": form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"livre":livre})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)
        livre.id = id;
        livre.save()
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})

def bibliotheque(request):
    livre = models.Livre.objects.all()
    return render(request,"bibliotheque/bibliotheque.html",{"livre":livre})
