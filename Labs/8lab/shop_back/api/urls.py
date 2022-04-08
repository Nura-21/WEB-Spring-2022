from django.urls import path
from api.views import products, each_product, categories, each_category, product_category

urlpatterns = [
    path('products/', products),
    path('products/<int:product_id>/', each_product),
    path('categories/', categories),
    path('categories/<int:category_id>/', each_category),
    path('categories/<int:category_id>/products', product_category),
]