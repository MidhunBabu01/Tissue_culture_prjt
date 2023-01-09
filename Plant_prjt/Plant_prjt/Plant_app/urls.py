from django.urls import path
from Plant_app import views


app_name = 'Plant_app'


urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about")
    
]
