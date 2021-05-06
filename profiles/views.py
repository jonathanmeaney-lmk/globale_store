from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order, OrderIssue


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all().order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def view_orders(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all().order_by('-date')

    template = 'profiles/view_orders.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def order_issue(request, order_number):

    user = get_object_or_404(User, username=request.user)
    order = get_object_or_404(Order, order_number=order_number)

    if request.method == 'POST' and request.user.is_authenticated:
        order = get_object_or_404(Order, order_number=order_number)
        issue_type = request.POST.get('order_issue_select')
        description = request.POST.get('description')
        user = get_object_or_404(User, username=request.user)
        email = request.POST.get('email')

        OrderIssue.objects.create(order=order, issue_type=issue_type, user=user, description=description, email=email)

        messages.success(request, 'Your issue has been logged. Will be in touch shortly.')

        return redirect(reverse('view_orders'))

    template = 'profiles/order_issue.html'
    context = {
        'order': order,
        'user': user
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)



