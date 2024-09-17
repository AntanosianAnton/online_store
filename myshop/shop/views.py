from django.shortcuts import render, get_object_or_404
from .models import Category, Product
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
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


"""получаем список товаров с категории New Drop"""


def product_list_new_drop(request):
    category = get_object_or_404(Category, slug='new-drop')
    products = Product.objects.filter(available=True, category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'products': products})


"""получаем список товаров с категории onesize"""


def product_list_onesize(request):
    category = get_object_or_404(Category, slug='futbolki-onesize')
    products = Product.objects.filter(available=True, category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'products': products})


"""получаем список товаров с категории oversize"""


def product_list_oversize(request):
    category = get_object_or_404(Category, slug='futbolki-oversize')
    products = Product.objects.filter(available=True, category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'products': products})


"""получаем список товаров с категории лонгслив"""


def product_list_longsleevs(request):
    category = get_object_or_404(Category, slug='longsleevs')
    products = Product.objects.filter(available=True, category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
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
