from django.db import models

class CarDetailes(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    briefdiscriptions = models.TextField(max_length=255)
    discription = models.TextField(max_length=255)
    image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    created_on = models.DateTimeField(auto_now_add=True)

