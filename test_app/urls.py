from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),	
    path ('log_out',views.log_out),
]
