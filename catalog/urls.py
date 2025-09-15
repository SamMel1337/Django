from django.urls import path
from .views import (ProductListView, ProductDetailView, BaseView, ContactsView,
                    ProductUpdateView, ProductCreateView)

app_name = 'catalog'

urlpatterns = [
    path("base/", BaseView.as_view(), name="base"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="home"),
    path("<int:pk>/delete/", ProductDetailView.as_view(), name="product_detail"),
    path('create/', ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit')
]