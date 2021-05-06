from products.models import Country, Category


def categories_countries(request):

    categories = Category.objects.all().order_by('name')
    countries = Country.objects.all().order_by('name')

    context = {
        'categories': categories,
        'countries': countries
    }

    return context
