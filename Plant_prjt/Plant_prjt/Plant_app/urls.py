from django.urls import path
from Plant_app import views


app_name = 'Plant_app'


urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('products/', views.products,name="products"),
    path('products-details/<slug:slug>', views.products_details,name="products_details"),
    path('contact-us/', views.contact_us,name="contact_us"),
    
    
    
]
