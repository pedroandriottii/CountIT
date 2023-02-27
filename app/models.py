from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self):
        return self.name
    


class Product(models.Model):
    title = models.CharField(max_length=65)
    salePrice = models.DecimalField(max_digits=10, decimal_places=2)
    purchasePrice = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    sold = models.IntegerField()
    barcode = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    
