from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Добавляет продукты в базу данных'

    def handle(self, *args, **kwargs):
        # Ваша логика
        self.stdout.write('Продукты добавлены')