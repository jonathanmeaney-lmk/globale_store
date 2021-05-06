from random import randint
from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.IntegerField()
    abv = models.DecimalField(max_digits=6, decimal_places=1)
    brewer = models.CharField(max_length=254, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def _generate_sku(self):
        """
        Generate a random sku number that starts with "gb"
        Code to generate random 10-digit number came from here:
        https://stackoverflow.com/questions/2673385/how-to-generate-random-number-with-the-specific-length-in-python
        """
        range_start = 10**9
        range_end = (10**10)-1
        x = randint(range_start, range_end)
        sku = f"gb{x}"
        return sku

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the sku number
        """
        if not self.sku:
            self.sku = self._generate_sku()
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name}'
