from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

from .models import ProductImage, Products, Category


def product_list(request, category_slug=None):

    category         = None 
    product_list     = Products.objects.all()
    category_list    = Category.objects.annotate(total_products=Count('products'))
    
    if category_slug:
        category     = get_object_or_404(Category,slug=category_slug)
        product_list = product_list.filter(category =category)

    search_query     = request.GET.get('q')

    if search_query:
        product_list = product_list.filter(
            Q(name__icontains                           = search_query) |
            Q(condition__icontains                      = search_query) |
            Q(description__icontains                    = search_query) |
            Q(brand__brand_name__icontains              = search_query) |
            Q(category__category_name__icontains        = search_query)
        )


    paginator        = Paginator(product_list, 6)
    page             = request.GET.get('page')
    product_list     = paginator.get_page(page) 
    template         = 'Products/product_list.html'
    context          = {
                        'product_list'  : product_list,
                        'category_list' : category_list,
                        'category'      : category
        }

    return render(request ,template, context)

def product_detail(request,product_slug):

    product_detail = get_object_or_404(Products,slug=product_slug)

    Product_image  = ProductImage.objects.filter(product=product_detail)

    template       = 'Products/product_detail.html'

    context        = {
                        'product_detail' : product_detail,
                        'product_image'  : Product_image
    }

    return render(request, template, context)
