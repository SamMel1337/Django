from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .permissions import is_moderator, is_owner


class ProductOwnerRequiredMixin(UserPassesTestMixin):
    """Mixin для проверки прав владельца или модератора"""
    def test_func(self):
        product = self.get_object()
        user = self.request.user

        if not user.is_authenticated:
            return False

        # Модераторы имеют доступ
        if is_moderator(user):
            return True

        # Владельцы имеют доступ к своим продуктам
        return is_owner(user, product)

    def handle_no_permission(self):
        raise PermissionDenied("У вас нет прав для выполнения этого действия")



class ProductDeleteMixin(ProductOwnerRequiredMixin):
    """Специальный mixin для удаления с дополнительными проверками"""

    def test_func(self):
        product = self.get_object()
        user = self.request.user

        if not user.is_authenticated:
            return False

        # Модераторы могут удалять любые продукты
        if is_moderator(user):
            return True

        # Владельцы могут удалять только свои продукты
        return is_owner(user, product)