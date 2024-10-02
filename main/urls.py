from django.urls import path
from . import views
from main.views import register, login_user, logout_user

app_name = 'main' 

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('create-product', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', views.show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>/', views.edit_product, name='edit_product'),
    path('delete-product/<uuid:id>/', views.delete_product, name='delete_product'),
    path('products/', views.products_view, name='products'),
    path('products/<int:category_id>/', views.products_view, name='products_by_category'),
    path('cart/', views.cart_view, name='cart'),
    path('categories/', views.categories_view, name='categories'),
    path('add-to-cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<uuid:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]




