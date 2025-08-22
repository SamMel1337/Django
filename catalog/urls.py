from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.example_view, name='base'),
    path('contacts/', views.example, name='contacts'),
    path('home/', views.example1, name='home'),
    path('product/<int:pk>/', views.product_list, name='product_list'),
]