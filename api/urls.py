from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . import views
router=routers.DefaultRouter()
router.register('set',views.Viewset,basename='set')

urlpatterns = [
   # path('api_view',views.HelloAPI.as_view()),
   # path('api_viewset/<int:api_pk>',views.HelloAPI.as_view())
   # path("api_viewset",include(router.urls))
   path('api_viewset',include(router.urls))
  
]
