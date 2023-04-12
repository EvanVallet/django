from django.shortcuts import render
from .forms import LivreForm
from . import models
def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"bibliotheque/affiche.html",{"livre" : livre})
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"bibliotheque/ajout.html",{"form": form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})

