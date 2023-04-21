from django.http import HttpResponseRedirect
from django.shortcuts import render
from videoGames.apiIA import prediction
from videoGames.forms import genreForm

def index(request):
    if request.method == 'POST':
        form = genreForm(request.POST)
        if form.is_valid(): 
            data = form.cleaned_data
            # Redirigez vers la page de prédiction avec les données du formulaire
            return HttpResponseRedirect('/predict?{}'.format(data.urlencode()))
    else:
        form = genreForm()
    return render(request, 'index.html', {'form': form})

def predict(request):
    # Récupérer les données du formulaire dans la requête GET
    platform = request.GET.get('platform')
    genre = request.GET.get('genre')
    year = request.GET.get('year')
    publisher = request.GET.get('publisher')
    na_sales = float(request.GET.get('na_sales'))
    jp_sales = float(request.GET.get('jp_sales'))
    global_sales = float(request.GET.get('global_sales'))

    result = prediction( {
            "platform": platform,
            "genre": genre,
            "year": year,
            "publisher": publisher,
            "na_sales": na_sales,
            "jp_sales": jp_sales,
            "global_sales": global_sales,
        })

    context = {
            "platform": platform,
            "genre": genre,
            "year": year,
            "publisher": publisher,
            "na_sales": na_sales,
            "jp_sales": jp_sales,
            "global_sales": global_sales,
            "result": result
        }
    
    return render(request, 'predict.html', context)
