from django.db import models
from .product_model import ProductBasic


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(ProductBasic, on_delete=models.CASCADE)
    quentity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_Status = models.BooleanField(default=False)
    coustomer_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    delivery_Address = models.CharField(max_length=1000)
    delivery_status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.product.name
