from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_stock = models.IntegerField()
    product_id = models.IntegerField()
    published_date = models.DateTimeField(blank=True, null=True)

    def Register(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.product_name