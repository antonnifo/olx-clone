from django.contrib import admin

from .models import Products,Category,Brand,ProductImage

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImage)
