from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


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
