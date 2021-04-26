from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Country, ProductReview
from django.contrib.auth.models import User


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    countries = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            products = products.filter(country__name__in=countries)
            categories = Country.objects.filter(name__in=countries)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_country': countries
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(User, username=request.user)
    reviews = product.reviews.all()

    if request.method == 'POST' and request.user.is_authenticated:
        rating = int(request.POST.get('rating', 3))
        content = request.POST.get('content', '')

        redirect_url = request.POST.get('redirect_url')

        review = ProductReview.objects.create(product=product, user=user, content=content, rating=rating)

        return redirect(redirect_url)

    print(reviews)

    context = {
        'product': product,
        'reviews': reviews
    }

    return render(request, 'products/product_detail.html', context)
