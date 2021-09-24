from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('api_viewset',views.HelloAPI.as_view())
]
