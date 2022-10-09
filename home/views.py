from multiprocessing import context
from django.shortcuts import render

from home.models import Brand, Category, New, Product

# Create your views here.


def index(request):
    caregoryList = Category.objects.all()
    productList = Product.objects.all()
    newsList = New.objects.all()
    context = {"caregoryList": caregoryList,
               "productList": productList, "newsList": newsList}
    # print(productList.id)
    print(caregoryList[0].id)

    return render(request, 'index.html', context)


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
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, 'details.html', context)


def search(request):

    return render(request, 'search.html')
