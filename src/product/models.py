from django.db import models

class Products(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    condition  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    created = models.DateTimeField()
