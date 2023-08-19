
from rest_framework import serializers
from .models import Property, PropertyType, CategoryType, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'video', 'image']
class propertytypeserializer(serializers.Serializer):
    class Meta:
        model = PropertyType
        fields=['name']

class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = ['id', 'name']

class PropertySerializer(serializers.ModelSerializer):
    property_type = serializers.StringRelatedField(source='property_type.name')
    category_type = CategoryTypeSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'property_type', 'category_type', 'images', 'address', 'country', 'city', 'total_rating', 'total_review']
    
class PropertyListSerializer(serializers.Serializer):
    data = PropertySerializer(many=True)


