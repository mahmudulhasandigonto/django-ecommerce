from django.contrib import admin

from home.models import Brand, Category, Contact, New, Product

# Register your models here.
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(New)
