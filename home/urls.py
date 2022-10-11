
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('fashion/', views.fashion, name='fashion'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('categorywise/<int:id>/', views.categorywise, name='categorywise'),
    path('details/<int:id>/', views.details, name='details'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('getcart/', views.getcart, name='getcart'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('validate_user/', views.validate_user, name='validate_user'),
    path('updateqnt/', views.updateqnt, name='updateqnt'),
    path('deleteFormCart/<int:id>', views.deleteFormCart, name='deleteFormCart'),

]
