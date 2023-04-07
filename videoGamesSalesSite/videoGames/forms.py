from django import forms

class genreForm(forms.Form):
    genre = forms.CharField(label='genre', max_length=100)
    year = forms.CharField(label='year', max_length=100)