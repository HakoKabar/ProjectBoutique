from django.urls.conf import path,include
from rest_framework import routers

from .views import CategoryViewset,ProductViewset

route =routers.DefaultRouter()
route.register('category',CategoryViewset,basename='c_ategory')
route.register('product',ProductViewset,basename='Product')


urlpatterns = [
    
    path('',include(route.urls)),


    
]