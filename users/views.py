from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/catalog/'  # или используйте reverse_lazy('название_пути')

    def form_valid(self, form):
        user = form.save()
        # Отправка приветственного письма
        send_mail(
            'Добро пожаловать!',
            'Спасибо за регистрацию в нашем магазине.',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        messages.success(self.request, 'Вы успешно зарегистрированы!')
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm  # если у вас есть кастомная форма входа
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = '/catalog/'

