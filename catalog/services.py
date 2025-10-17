# catalog/services.py
from django.core.cache import cache
from django.conf import settings
from .models import Product, Category


def get_products_by_category(category_slug):
    """
    Получает продукты по slug категории с кешированием
    """
    cache_key = f'products_category_{category_slug}'

    if settings.CACHE_ENABLED:
        products = cache.get(cache_key)
        if products is not None:
            return products

    try:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(
            category=category,
            is_published=True
        ).select_related('category').prefetch_related('images')
    except Category.DoesNotExist:
        products = Product.objects.none()

    if settings.CACHE_ENABLED:
        cache.set(cache_key, products, timeout=3600)  # Кешируем на 1 час

    return products


def get_category_by_slug(category_slug):
    """
    Получает категорию по slug
    """
    try:
        return Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
        return None