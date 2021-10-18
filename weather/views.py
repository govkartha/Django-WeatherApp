import requests
from django.views.generic import View
from django.shortcuts import redirect, render

from .models import City
from weather.forms import CityForm

# Create your views here.
# class indexView(View):
#     def get():
#         return render(request, 'weather/weather.html')

def indexView(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6c542977ec25cf56e254e37b65449da8'
    message,message_class = '',''
    if(request.method == 'POST'):
        form = CityForm(request.POST)

        if(form.is_valid()):
            new_city = form.cleaned_data['name']
            exsisting_city_count = City.objects.filter(name__iexact=new_city).count()

            if(exsisting_city_count == 0):
                r = requests.get(url.format(new_city)).json()

                if(r['cod']==200):
                    form.save()
                else:
                    message = r['message']
                    message_class = 'is-danger'
            else:
                message = "City already exists!"
                message_class = 'is-danger'

    form = CityForm()
    weather_data = []
    for city in City.objects.all():
        r = requests.get(url.format(city)).json()
        weather_info = {
            'city':city.name,
            'temp': int(5/9 * (r['main']['temp']-32)),
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }
        weather_data.append(weather_info)
    context = {
        'weather_data':weather_data,
        'form':form,
        'message':message,
        'message_class':message_class
    }
    return render(request, 'weather/weather.html',context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')