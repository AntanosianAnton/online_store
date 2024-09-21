from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page,
         name='main_page'),
    path('shop/list', views.product_list, name='product_list'),
    path('shop/futbolki/', views.product_list_futbolki,
         name='product_list_futbolki'),
    path('shop/longsleevs/', views.product_list_longsleevs,
         name='product_list_longsleevs'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<slug:slug>/<int:id>/', views.product_detail,
         name='product_detail'),
    path('shop/delivery_payments/', views.delivery_payments,
         name='delivery_payments'),
    path('shop/contacts/', views.contacts, name='contacts'),
    path('shop/exchange_return/', views.exchange_return,
         name='exchange_return'),
]
