from rest_framework import serializers
from . models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    # field level validation    
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value
    
    # object level validation
    def validate(self,attrs):
        if not attrs.get('is_published') and attrs.get('price') > 1000:
            raise serializers.ValidationError("Unpublished books cannot be more than 1000")
        return attrs
