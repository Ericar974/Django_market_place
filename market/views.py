from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect, request
from django.views.generic import ListView

from market.models import Test
from market.forms import TestForm
# Create your views here.

# liste


def index(request):
    tests = Test.objects.all().order_by('id')  # Obtenez de la valeur
    # Passer une valeur au modèle
    return render(request, 'market/index.html', {'tests': tests})


#Liste (ajoutée pour la nation de la page)
class TestList(ListView):
	model = Test #Modèle à utiliser
	context_object_name='tests' #Paramètre de nom d'objet (la valeur par défaut est object_Ça devient une liste)
	template_name='market/index.html' #Spécifier une page de modèle
	paginate_by = 9 #Nombre de pages par page

# Nouveau et modifier

def edit(request, id=None):

	if id: #Lorsqu'il y a un identifiant (lors de l'édition)
		#Rechercher par identifiant et renvoyer les résultats ou erreur 404
		tests = get_object_or_404(Test, pk=id)
	else: #Quand il n'y a pas d'identifiant (quand neuf)
		#Créer un membre
		tests = Test()

	#Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
	if request.method == 'POST':
		#Générer un formulaire
		form = TestForm(request.POST, instance=tests)
		if form.is_valid(): #Enregistrer si la validation est OK
			tests = form.save(commit=False)
			tests.save()
			return redirect('market:index')
	else: #Au moment de GET (générer un formulaire)
		form = TestForm(instance=tests)
	
	#Afficher un nouvel écran / modifier l'écran
	return render(request, 'market/edit.html', dict(form=form, id=id))
	#return HttpResponse("Éditer")

# Effacer
def delete(request, id):
	# return HttpResponse("Effacer")
	tests = get_object_or_404(Test, pk=id)
	tests.delete()
	return redirect('market:index')

# Détails (bonus)
def detail(request, id):
    tests = get_object_or_404(Test, pk=id)
    return render(request, 'market/detail.html', {'tests':tests})