from multiprocessing import context
import re
from django.shortcuts import render, redirect

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
    # For Subtotal
    cartList = Cart.objects.all()
    total = 0
    for cart in cartList:
        total = total + (cart.cart_price * cart.cart_quantity)

    sub_total = (total/100)*5+total
    context = {'cartList': cartList, "sub_total": sub_total}

    return render(request, 'cart.html', context)


def getcart(request):
    cartList = Cart.objects.all()
    total = 0
    for cart in cartList:
        total = total + (cart.cart_price * cart.cart_quantity)

    sub_total = (total/100)*5 + total
    context = {'cartList': cartList, 'sub_total': sub_total}

    if len(cartList) > 0:
        return render(request, 'cart.html', context)
    return redirect('/index/')


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
    return redirect('/getcart/')


def login(request):

    return render(request, 'login.html')


def registration(request):

    return render(request, 'registration.html')


def validate_user(request):
    user_email = request.POST.get('email')
    user_password = request.POST.get('password')

    return redirect('/index/')


def handle_not_found(request, exception):
    return render(request, 'notfound.html')


def updateqnt(request):
    qnt = request.GET.get('qnt')
    id = int(request.GET.get('id'))

    cart = Cart.objects.get(id=id)
    cart.cart_quantity = int(qnt)
    cart.save()
    return redirect('/getcart/')
