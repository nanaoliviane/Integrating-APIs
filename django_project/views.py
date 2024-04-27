import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  response = requests.get("https://swapi-api.alx-tools.com/api/films/7/")
  film_data = response.json()
  return render(request, 'templates/index.html', {'film_data': film_data})
    
  
  