import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


# Create your views here.

def index(request):
    appid = '086f7016c78ca1cc36164f22cc73d8f2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    # city = 'London'

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        print(res)
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'wind': res['wind']['speed'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    

    context = {'all_info': all_cities, 'form': form}

    return render(request, "index.html", context)
