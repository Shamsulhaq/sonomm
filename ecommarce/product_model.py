from django.db import models
from django.db.models.signals import pre_save
from sonomm.utils import unique_slug_generator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Create Product Model here.
class ProductBasic(models.Model):
    name = models.CharField(max_length=200,default='Product name', help_text='Enter your Product Title')
    category = models.ManyToManyField(Category)
    regular_price = models.DecimalField(max_digits=9, decimal_places=2, default=100.00, blank=True, null= True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=100.00)
    sortDec = models.TextField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to='productThm', blank=True)
    is_Feature = models.BooleanField(default=True)
    is_newAriavle = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

class ProductGallery(models.Model):
    product = models.OneToOneField(ProductBasic, on_delete=models.CASCADE)
    image2 = models.ImageField(upload_to='productGallery', blank=True)
    image3 = models.ImageField(upload_to='productGallery', blank=True)
    image4 = models.ImageField(upload_to='productGallery', blank=True)
    image5 = models.ImageField(upload_to='productGallery', blank=True)

    def __str__(self):
        return self.product.title



def pd_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pd_pre_save_receiver, sender=ProductBasic)


