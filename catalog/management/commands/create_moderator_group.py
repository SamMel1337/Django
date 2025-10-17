from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу модераторов с необходимыми правами'

    def handle(self, *args, **options):
        # Создаем или получаем группу
        group, created = Group.objects.get_or_create(name='moderators')

        if created:
            self.stdout.write('✅ Группа модераторов создана')
        else:
            self.stdout.write('⚠️  Группа модераторов уже существует')

        # Добавляем права на управление продуктами
        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(content_type=content_type)

        for perm in permissions:
            group.permissions.add(perm)

        self.stdout.write('✅ Права добавлены в группу модераторов')