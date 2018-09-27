from django.db import models
from django.db.models.signals import pre_save
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template

from .product_model import ProductBasic


# Create your models here.
class Order(models.Model):
    DELIVERY_STATUS = (
        ('o', 'Office Pick'),
        ('h', 'Home Delivery'),
    )

    product = models.ForeignKey(ProductBasic, models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=150, help_text="Enter Your Fullname")
    email = models.EmailField(help_text='Enter Your Email ')
    phone = models.CharField(max_length=15, help_text='Enter Your phone ')
    address = models.CharField(help_text='Enter your Delivery Address',max_length=250)
    area = models.CharField(help_text='Enter your Area name',max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    delivery_Method = models.CharField(max_length=1, choices=DELIVERY_STATUS, default=None,blank=True,null=True)
    is_confirm = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,auto_now_add=False)

    class Meta:
        ordering = ['-timestamp']

    def total_price(self):
        return self.price * self.quantity

    def delivery_price(self):
        if self.delivery_Method == 'h':
            return self.total_price() + 100
        else:
            return self.total_price()

    def __str__(self):
        return self.product.name


def pd_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.is_paid:
        messa = {
            'Customer_name': instance.name,
        }
        mail_subject = 'Payment Successful'
        message = get_template('mail/thanks_mail.html').render(messa)
        to_email = instance.email
        email_from = settings.EMAIL_HOST_USER
        email = EmailMessage(
            mail_subject, message, email_from, to=[to_email]
        )
        email.content_subtype = 'html'
        email.send()


pre_save.connect(pd_pre_save_receiver, sender=Order)
