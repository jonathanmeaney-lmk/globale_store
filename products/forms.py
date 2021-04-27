from django import forms
from .models import Product, Category, Country


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        countries = Country.objects.all()
        country_friendly_names = [(c.id, c.get_friendly_name()) for c in countries]

        self.fields['category'].choices = category_friendly_names
        self.fields['country'].choices = country_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-form-input'
