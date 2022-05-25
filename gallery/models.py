
from django.db import models

# Create your models here.
class Image(models.Model):
    image_file = models.ImageField(width_field=None, upload_to = 'gallery', height_field= None)