from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('secret', views.secret),
    path('secret/ultra_secret', views.ultra_secret),
    path('cars', views.cars),
]
