
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('fashion/', views.fashion, name='fashion'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
]