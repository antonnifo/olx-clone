from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

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
    brand       = models.ForeignKey('Brand',on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500)
    condition   = models.CharField(max_length=100, choices=CONDITION_TYPE)
    price       = models.DecimalField(max_digits=11,decimal_places=2)
    image   = models.ImageField(upload_to='main_product/', blank=True, null=True)
    created     = models.DateTimeField(default=timezone.now)
    
    slug        = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        '''overrides save action'''
        
        if not self.slug and self.name:
            self.slug = slugify(self.name)

        super(Products, self).save(*args, **kwargs)    

    class Meta:
        verbose_name        = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Products,  on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='product/', blank=True, null=True)

    class Meta:
        verbose_name        = 'Product_image'
        verbose_name_plural = 'Product_images'

    def __str__(self):
        return self.product.name

class Category(models.Model):
    
    category_name = models.CharField(max_length=50)
    image         = models.ImageField(upload_to='category/', blank=True,null=True)

    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
    

class Brand(models.Model):
    
    brand_name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name        = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name