from django.shortcuts import render
from .models import Products

def product_list(request):

    product_list = Products.objects.all()

    template     = 'Products/product_list.html'

    context      = {
                    'product_list' : product_list
        }

    return render(request ,template, context)

def product_detail(request,product_slug):

    product_detail = Products.objects.get(slug=product_slug)

    template       = 'Products/product_detail.html'

    context        = {
                        'product_detail' : product_detail
    }

    return render(request, template, context)
   