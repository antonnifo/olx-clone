from django.core.paginator import Paginator
from django.shortcuts import render

from .models import ProductImage, Products, Category


def product_list(request):

    product_list  = Products.objects.all()

    category_list = Category.objects.all() 

    template      = 'Products/product_list.html'

    paginator     = Paginator(product_list, 1)

    page          = request.GET.get('page')

    product_list  = paginator.get_page(page) 

    context       = {
                    'product_list'  : product_list,
                    'category_list' : category_list
        }

    return render(request ,template, context)

def product_detail(request,product_slug):

    product_detail = Products.objects.get(slug=product_slug)

    Product_image  = ProductImage.objects.filter(product=product_detail)

    template       = 'Products/product_detail.html'

    context        = {
                        'product_detail' : product_detail,
                        'product_image'  : Product_image
    }

    return render(request, template, context)
