from django.db import models
from .product_model import ProductBasic
from django.db.models.signals import pre_save


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(ProductBasic, models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=150, help_text="Enter Your Fullname")
    email = models.EmailField(help_text='Enter Your Email ')
    phone = models.CharField(max_length=15, help_text='Enter Your phone ')
    address = models.TextField(help_text='Enter your Delivery Address')
    quentity = models.PositiveIntegerField(default=1)
    is_confirm = models.BooleanField(default=False)
    is_onprocess = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def total_price(self):
        return self.price * self.quentity

    def __str__(self):
        return self.product.name


def pd_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.is_done:
        instance.is_onprocess = False


pre_save.connect(pd_pre_save_receiver, sender=Order)
