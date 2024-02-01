from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('delivery_payments/', views.delivery_payments,
         name='delivery_payments'),
    path('contacts/', views.contacts, name='contacts'),
    path('exchange_return/', views.exchange_return,
         name='exchange_return'),
]
