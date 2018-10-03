from django.db import models


class InspiringRemark(models.Model):
    author = models.CharField(max_length=155)
    remarks = models.TextField()
    image = models.ImageField(upload_to='inspiring/author/img', blank=True, null=True)
    des = models.CharField(max_length=255)
    fb = models.CharField(max_length=255, blank=True, null=True,default='#')
    twi = models.CharField(max_length=255, blank=True, null=True,default='#')
    sky = models.CharField(max_length=255, blank=True, null=True,default='#')
    active = models.BooleanField(default=True)
    is_in_font = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
