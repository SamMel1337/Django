from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from catalog.models import Product
from .forms import ProductForm


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')  # или другой URL, куда перенаправлять после создания


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})