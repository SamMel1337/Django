from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.files import File
from django.core.files.images import ImageFile
import os
from django.conf import settings
from io import BytesIO


class Command(BaseCommand):
    help = 'Add Products and Categories to database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category1, _ = Category.objects.get_or_create(name='Овощи', description='Полезные и питательные')
        category2, _ = Category.objects.get_or_create(name='Фрукты', description='Сладкие и вкусные')

        # Path to the image file (relative to MEDIA_ROOT)
        image_name = 'background.png'
        image_path = os.path.join(settings.MEDIA_ROOT, 'image', image_name)

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(image_path), exist_ok=True)

        # Create a dummy image if it doesn't exist
        if not os.path.exists(image_path):
            self.stdout.write(self.style.WARNING(f'Creating placeholder image at {image_path}'))
            with open(image_path, 'wb') as f:
                f.write(b'')  # Creates empty file

        # Read image content and prepare file objects
        with open(image_path, 'rb') as img_file:
            image_content = img_file.read()

            products = [
                {'name': 'Яблоко', 'description': 'Зеленое', 'category': category2, 'price': 100},
                {'name': 'Ананас', 'description': 'Колючий', 'category': category2, 'price': 200},
                {'name': 'Капуста', 'description': 'Укутанная', 'category': category1, 'price': 80},
                {'name': 'Кукуруза', 'description': 'Желтая', 'category': category1, 'price': 120},
                {'name': 'Груша', 'description': 'Ламповидная', 'category': category2, 'price': 250},
                {'name': 'Абрикос', 'description': 'Ядровой', 'category': category2, 'price': 180},
                {'name': 'Томат', 'description': 'Коктельные', 'category': category1, 'price': 110}
            ]

            for product_data in products:
                # Create new in-memory file for each product
                file_obj = BytesIO(image_content)
                product_data['image'] = ImageFile(file_obj, name=image_name)

                product, created = Product.objects.get_or_create(
                    name=product_data['name'],
                    defaults=product_data
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))