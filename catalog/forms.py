from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Product, Category


class ProductForm(forms.ModelForm):
    BANNED_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'is_published']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'})
        }
        labels = {
            'price': 'Цена (руб)'
        }
        error_messages = {
            'price': {
                'invalid': "Введите корректное числовое значение цены",
            }
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None:
            if price < 0:
                raise ValidationError(
                    "Цена не может быть отрицательной. Введите положительное значение.",
                    code='price_negative'
                )
            if price > 1000000:  # Дополнительная валидация на максимальную цену
                raise ValidationError(
                    "Цена слишком высокая. Максимальная цена - 1 000 000 руб.",
                    code='price_too_high'
                )

        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].required = True

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        for word in self.BANNED_WORDS:
            if word in name:
                raise forms.ValidationError(f'Название содержит запрещенное слово: "{word}"')
        return self.cleaned_data['name']

    def clean_description(self):
        description = self.cleaned_data['description'].lower()
        for word in self.BANNED_WORDS:
            if word in description:
                raise forms.ValidationError(f'Описание содержит запрещенное слово: "{word}"')
        return self.cleaned_data['description']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_field_styles()

    def set_field_styles(self):
        """Устанавливает классы CSS для всех полей формы"""
        for field_name, field in self.fields.items():
            # Добавляем стандартный класс form-control для всех полей
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'


class ModeratorForm(StyleFormMixin , ModelForm):
    class Meta:
        model = Product
        fields = ("description","name")
