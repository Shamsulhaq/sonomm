from django.db import models
from .product_model import ProductBasic


class Slider(models.Model):
    heading = models.CharField(max_length=250, help_text='Enter Title Text')
    sortDis = models.TextField()
    image_file = models.ImageField(upload_to='Slider/image', null=True)
    buttonText = models.CharField(max_length=100, help_text='button title text')
    buttonUrl = models.CharField(max_length=250, help_text='Url')
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class LimitedOffer(models.Model):
    product = models.ForeignKey(ProductBasic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Offer/img',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_date= models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title


class GetEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
