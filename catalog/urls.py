from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('base/', views.example_view, name='base'),
    path('contacts/', views.example, name='contacts'),
    path('home/', views.example1, name='home')
]