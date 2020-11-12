from django.shortcuts import render 
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializer import * 
  
class ReactView(APIView): 
    serializer_class = ReactSerializer

    def get(self, request): 
        detail = [{
          "url_code": detail.url_code,
          "long_url": detail.long_url,
          "short_url": detail.short_url,
          }  
        for detail in React.objects.all()] 
        return Response(detail) 
  
    def post(self, request):
        serializer = ReactSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data)
