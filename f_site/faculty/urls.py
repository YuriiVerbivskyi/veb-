from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('specialities/', views.specialities_list, name = 'specialities'),
    path('specialities/<int:id>/', views.specialities_detail, name = 'specialities_detail'),
    path('departments/', views.department_list, name = 'department_list'),
    path('departments/<int:id>/', views.department_detail, name = 'department_detail')
]