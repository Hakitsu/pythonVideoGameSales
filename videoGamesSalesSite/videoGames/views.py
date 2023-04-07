from django.http import HttpResponseRedirect
from django.shortcuts import render

from videoGames.forms import genreForm

from fastapi import FastAPI

app = FastAPI()

def index(request):
      if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = genreForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            data = form.cleaned_data['genre', 'year']
            return render(request, 'predict.html', {'data': data})

    # if a GET (or any other method) we'll create a blank form
      else:
        form = genreForm()
      return render(request, 'index.html', {'form': form})


@app.post("/predict/")
async def predict(request):
    
    platform = request.POST['platform']
    genre = request.POST['genre']
    year = request.POST['year']
    publisher =request.POST['publisher']
    na_sales = request.POST['na_sales']
    jp_sales= request.POST['jp_sales']
    global_sales = request.POST['global_sales']

    context = {
            "platform": platform,
            "genre": genre,
            "year": year,
            "publisher": publisher,
            "na_sales": na_sales,
            "jp_sales": jp_sales,
            "global_sales": global_sales
        }
    
    return render(request, 'predict.html', context)