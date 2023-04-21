from django.http import HttpResponseRedirect
from django.shortcuts import render
from videoGames.apiIA import prediction

from videoGames.forms import genreForm

from fastapi import FastAPI

app = FastAPI()

def index(request):
      if request.method == 'POST':
        form = genreForm(request.POST)
        if form.is_valid(): 
            data = form.cleaned_data['genre', 'year']
            return render(request, 'predict.html', {'data': data})
      else:
        form = genreForm()
      return render(request, 'index.html', {'form': form})


@app.post("/predict/")
async def predict(request):
    platform = request.POST['platform']
    year = request.POST['year']
    genre = request.POST['genre']
    publisher =request.POST['publisher']
    na_sales = request.POST['na_sales']
    jp_sales= request.POST['jp_sales']
    global_sales = request.POST['global_sales']

    result = prediction( {
            "platform": platform,
            "year": year,
            "genre": genre,
            "publisher": publisher,
            "na_sales": na_sales,
            "jp_sales": jp_sales,
            "global_sales": global_sales,
        })

    context = {
            "platform": platform,
            "year": year,
            "genre": genre,
            "publisher": publisher,
            "na_sales": na_sales,
            "jp_sales": jp_sales,
            "global_sales": global_sales,
            "result": result
        }
    
    return render(request, 'predict.html', context)