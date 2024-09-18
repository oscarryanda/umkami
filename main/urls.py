from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-product', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', views.show_json_by_id, name='show_json_by_id'),  # Changed <str:id> to <uuid:id>
]
