from django.urls import path
from Plant_app import views

urlpatterns = [
    path('', views.index,name="index")
]
