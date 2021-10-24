
from django.db.models.query_utils import Q
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet


from .models import Category,Product
from .serializer import CategorySerializer,ProductSerializer


class CategoryViewset(ReadOnlyModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(ModelViewSet):
    
    serializer_class=ProductSerializer
    def get_queryset(self):
        queryset=Product.objects.filter(active=True)
        numero_de_category=self.request.GET.get('numero/de/category')
      
        if numero_de_category  :
            queryset =queryset.filter(category=numero_de_category)
            return queryset
        else :
            product_noactive=self.request.GET.get('product/noactive')
           
            if product_noactive : 
                queryset=Product.objects.all()
                queryset=queryset.filter(active=product_noactive)
            return queryset
  


        

        


    
