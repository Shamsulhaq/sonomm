from django.db import models
from django.db.models.signals import pre_save
from sonomm.utils import unique_slug_generator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/main', blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    mainCat = models.ForeignKey(Category, on_delete=models.CASCADE);
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/sub', blank=True)

    def __str__(self):
        return self.name

    def get_category_main(self):
        return self.mainCat.name


# Create Product Model here.
class ProductBasic(models.Model):
    name = models.CharField(max_length=200, help_text='Enter your Product Title')
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    regular_price = models.DecimalField(max_digits=9, decimal_places=2, default=100.00, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=100.00)
    unit = models.CharField(help_text='Enter unity deviate by comma', max_length=200)
    sortDec = models.TextField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to='products/thumbnail', blank=True)
    is_Feature = models.BooleanField(default=True)
    is_newAriavle = models.BooleanField(default=True)
    is_slide = models.BooleanField(default=False)
    is_Friday = models.BooleanField(default=False)
    is_stock = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def __str__(self):
        return self.name

    def get_category(self):
        return self.category.name

    def get_discunt(self):
        dis = ((self.regular_price - self.price) / self.regular_price) * 100
        discubt = int(dis)
        return discubt

    @property
    def title(self):
        return self.name


class ProductGallery(models.Model):
    product = models.ForeignKey(ProductBasic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/Gallery', blank=True)

    def __str__(self):
        return self.product.title


def pd_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pd_pre_save_receiver, sender=ProductBasic)
