from django.http import HttpResponseRedirect
from django.shortcuts import render

from videoGames.forms import genreForm

def index(request):
      if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = genreForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

        
            
            data = form.cleaned_data['genre', 'year']
            return render(request, 'predict.html', {'data': data})

    # if a GET (or any other method) we'll create a blank form
      else:
        form = genreForm()
      return render(request, 'index.html', {'form': form})


def predict(request):
    genre = request.POST['genre']
    year = request.POST['year']
    context = {
            "genre": genre,
            "year": year
        }
    return render(request, 'predict.html', context)