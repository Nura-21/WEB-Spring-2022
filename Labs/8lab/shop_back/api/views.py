from django.http import JsonResponse
from api.models import Category, Product

def products(request):
    products = Product.objects.all()
    products_json = [product.makeJson() for product in products]
    return JsonResponse(products_json, safe=False, json_dumps_params={'indent' : 4})


def each_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return JsonResponse(product.makeJson(), safe=False, json_dumps_params={'indent' : 4})


def categories(request):
    categories = Category.objects.all()
    categories_json = [category.makeJson() for category in categories]
    return JsonResponse(categories_json, safe=False, json_dumps_params={'indent' : 4})


def each_category(request, category_id):
    category = Category.objects.get(id=category_id)
    return JsonResponse(category.makeJson(), safe=False, json_dumps_params={'indent' : 4})

def product_category(request, category_id):
    products = Product.objects.filter(cat_id=category_id) 
    products_categories = [product.makeJson() for product in products]
    return JsonResponse(products_categories, safe=False, json_dumps_params={'indent' : 4})
