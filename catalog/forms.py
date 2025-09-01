from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем класс 'form-control' ко всем полям формы
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            classes = existing_classes + ' form-control'
            field.widget.attrs['class'] = classes.strip()

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        self._check_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        self._check_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Цена не может быть пустой.")
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    def _check_forbidden_words(self, text):
        text_lower = text.lower()
        for word in FORBIDDEN_WORDS:
            if word in text_lower:
                raise forms.ValidationError(
                    f"Использование слова '{word}' запрещено."
                )