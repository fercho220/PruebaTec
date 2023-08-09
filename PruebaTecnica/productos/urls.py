from django.urls import path
from productos import views
urls_productos = [path('register_product/',views.register_product),
                  path('update_product/<int:_id>/',views.details_product),
                  path('all_product/',views.get_products),
                  path('delete_product/<int:_id>/',views.delete_product),]