from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/', views.view_orders, name='view_orders'),
    path('order_issue/<order_number>', views.order_issue, name='order_issue'),
    path('order_history/<order_number>', views.order_history, name='order_history'),

]