from django.shortcuts import render
import json
# from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
# Create your views here.

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
        return Response(serializer.data )
    return Response({'invalid':'invalid data'}, status=400)