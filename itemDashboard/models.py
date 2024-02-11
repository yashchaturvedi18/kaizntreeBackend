from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)
    category = models.CharField(max_length=100)  # You might want to create a separate Category model
    tags = models.CharField(max_length=255)
    stock_status = models.CharField(max_length=20, choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')])
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name