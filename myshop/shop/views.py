from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductSize
from cart.forms import CartAddProductForm

"""получаем список всех товаров"""


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    products = products.order_by('-created')
    for product in products:
        product.available_sizes = ProductSize.objects.filter(
            product=product,
            available=True).select_related('size')
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


"""получаем список товаров с категории футболки"""


def product_list_futbolki(request):
    category = get_object_or_404(Category, slug='futbolki')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, category=category)
    products = products.order_by('-created')
    for product in products:
        product.available_sizes = ProductSize.objects.filter(
            product=product,
            available=True).select_related('size')

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


"""получаем список товаров с категории лонгслив"""


def product_list_longsleevs(request):
    category = get_object_or_404(Category, slug='longsleevs')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True, category=category)
    products = products.order_by('-created')
    for product in products:
        product.available_sizes = ProductSize.objects.filter(
            product=product,
            available=True).select_related('size')

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    # Получаем все изображения продукта
    images = product.images.all()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'images': images})


def delivery_payments(request):
    return render(request, 'shop/delivery_payments.html')


def contacts(request):
    return render(request, 'shop/contacts.html')


def exchange_return(request):
    return render(request, 'shop/exchange_return.html')


def main_page(request):
    return render(request, 'shop/main_page.html')
