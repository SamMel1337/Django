from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


# Перевод списка товаров
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

# Детальный просмотр товара
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# Страница base
class BaseView(TemplateView):
    template_name = 'catalog/base.html'

# Страница контактов
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

# Главная страница (home)
class HomeView(TemplateView):
    template_name = 'catalog/home.html'