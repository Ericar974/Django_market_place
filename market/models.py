from django.utils import timezone
import datetime
from django.db import models

# Create your models here.
 
class Test(models.Model):
    text = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField()
    img = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField('date')#'text', 'price', 'img', 'stock', 'description'
    def __str__(self):
        return self.text
    def publier(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
