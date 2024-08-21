from django.shortcuts import render
from rest_framework import authentication, generics, mixins, permissions
from . models import Product
from . serializers import ProductSerializer
from api.authentication import TokenAuthentication
from . permissions import isStaffEditorPermission
# Create your views here.


# ===================
# this is product create view
# ===================
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes=[
        authentication.SessionAuthentication,
        TokenAuthentication
    ]
    permission_classes=[permissions.IsAdminUser,isStaffEditorPermission]
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
        serializer.save(content=content)
product_list_create_view = ProductListCreateAPIView.as_view()


# ===================
# this is product retrieve view
# ===================
class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
product_details_view = ProductDetailsAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
product_list_view = ProductListAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not serializer.content:
            instance.content = instance.title
        
        
product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
product_delete_api = ProductDestroyAPIView.as_view()

'''
=======================

        model mixin start from here
        
=======================
'''

'''  '''
class productListMixinView(
        generics.ListAPIView,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin, 
        mixins.CreateModelMixin
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = 'this is the default content'
            
        serializer.save(content=content)
            
product_mixins_list = productListMixinView.as_view()