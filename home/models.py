from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=250)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name + " | " + self.message


class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(
        upload_to='media', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_Description = models.TextField(max_length=500)
    product_img = models.ImageField(
        upload_to='images', height_field=None, width_field=None, max_length=100)
    product_name = models.CharField(max_length=225)
    product_price = models.FloatField()

    def __str__(self):
        return self.product_name
