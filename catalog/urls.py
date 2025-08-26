from django.urls import path
from .views import ProductListView ,ProductDetailView , BaseView ,ContactsView

app_name = 'catalog'

urlpatterns = [
    path("base/", BaseView.as_view(), name="base"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="home"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]