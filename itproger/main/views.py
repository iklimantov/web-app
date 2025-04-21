from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'food': 'Pizza',
            'age': 22,
            'hobby': 'Tourism'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def cars(request):
    return render(request, 'main/cars.html')

def secret(request):
    return HttpResponse("<h1>Поздравляю! Вы нашли секретную страницу<h1>")

def ultra_secret(request):
    return HttpResponse("<h1>Поздравляю! Вы нашли УЛЬТРА секретную страницу<h1>")
