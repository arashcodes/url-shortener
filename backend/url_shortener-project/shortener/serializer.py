from rest_framework import serializers 
from . models import *
  
class ReactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Shortener 
        fields = ['url_code', 'long_url', 'short_url', 'created_at']
