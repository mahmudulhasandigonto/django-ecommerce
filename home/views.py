from multiprocessing import context
from django.shortcuts import render

from home.models import Brand, Category, Product

# Create your views here.


def index(request):
    caregoryList = Category.objects.all()
    productList = Product.objects.all()
    context = {"caregoryList": caregoryList}
    # print(productList.id)
    print(caregoryList[0].id)

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def products(request):
    return render(request, 'products.html')


def fashion(request):
    return render(request, 'fashion.html')


def news(request):
    return render(request, 'news.html')


def categorywise(request, id):
    categoryList = Category.objects.all()
    productList = Product.objects.filter(category=id)
    print(productList)
    context = {"categoryList": categoryList, 'productList': productList}
    return render(request, 'categorywise.html', context)
