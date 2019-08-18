from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Products(models.Model):

    CONDITION_TYPE = (
        ("New","New"),
        ("Used for less than a Month","Used for less than a Month"),
        ("Used for less than  3 Months","Used for less than 3 Months"),
        ("Used for less than  6 Months","Used for less than 6 Months"),
        ("Used for more than  6 Months","Used for more than 6 Months")
        
    )
    
    name        = models.CharField(max_length=100)
    owner       = models.ForeignKey(User, on_delete=models.CASCADE)
    category    = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500)
    condition   = models.CharField(max_length=100, choices=CONDITION_TYPE)
    price       = models.DecimalField(max_digits=11,decimal_places=2)
    created     = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name        = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
    
class Category(models.Model):
    
    category_name = models.CharField(max_length=50)
    image         = models.ImageField(upload_to='products/', blank=True,null=True)

    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
    
