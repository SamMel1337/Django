from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path("", views.example_view, name="base"),
    path("contacts/", views.example, name="contacts"),
    path("home/", views.product_list, name="home"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
]