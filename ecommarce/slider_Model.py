from django.db import models


class Slider(models.Model):
    heading     = models.CharField(max_length=250, help_text='Enter Title Text')
    sortDis     = models.TextField()
    image_file  = models.ImageField(upload_to='Slider/image', null=True)
    buttonText  = models.CharField(max_length=100, help_text='button title text')
    buttonUrl   = models.CharField(max_length=250, help_text='Url')

    def __str__(self):
        return self.heading


