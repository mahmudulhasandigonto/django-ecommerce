from multiprocessing import context
from django.shortcuts import render

from home.models import Brand, Cart, Category, New, Product

# Create your views here.


def index(request):
    caregoryList = Category.objects.all()
    productList = Product.objects.all()
    newsList = New.objects.all()
    context = {"caregoryList": caregoryList,
               "productList": productList, "newsList": newsList}

    return render(request, 'index.html', context)


def cart(request):
    qnt = request.GET.get('quantity')
    product_id = request.GET.get('product_id')
    if len(Cart.objects.filter(product_id=product_id)) < 1:
        product = Product.objects.get(id=product_id)
        cart = Cart(product_id=product_id, cart_name=product.product_name,
                    cart_price=product.product_price, cart_tax=5, cart_quantity=qnt)
        cart.save()

    cartList = Cart.objects.all()
    # cartList.delete()
    context = {'cartList': cartList}

    return render(request, 'cart.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def products(request):
    productList = Product.objects.all()
    context = {"productList": productList}
    return render(request, 'products.html', context)


def fashion(request):

    return render(request, 'fashion.html')


def news(request):
    newsList = New.objects.all()

    context = {'newsList': newsList}

    return render(request, 'news.html', context)


def categorywise(request, id):

    categoryList = Category.objects.all()
    productList = Product.objects.filter(category=id)
    newsList = New.objects.all()
    print(productList)
    context = {"categoryList": categoryList,
               'productList': productList, "newsList": newsList}
    return render(request, 'categorywise.html', context)


def details(request, id):
    newsList = New.objects.all()
    product = Product.objects.get(id=id)
    context = {"product": product, "newsList": newsList}
    return render(request, 'details.html', context)


def search(request):
    query = request.GET.get('query')
    productList = Product.objects.filter(product_name__icontains=query)

    context = {"productList": productList}
    return render(request, 'search.html', context)


def deleteFormCart(request, id):
    cart = Cart.objects.filter(id=id)
    cart.delete()
    return render(request, 'cart.html')
