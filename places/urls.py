from django.urls import path
from places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/', views.places_list, name='places_list'),
    path('places/add/', views.add_place, name='add_place'),
    path('places/random/', views.random_place, name='random_place'),
    path('places/<int:index>/', views.place_detail, name='place_detail'),
]
