
from rest_framework import serializers
from .models import Property, PropertyType, CategoryType, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'video', 'image']

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ['name']

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


# class PropertyListSerializer(serializers.Serializer):
#     limit = serializers.IntegerField(required=False)
#     offset = serializers.IntegerField(required=False)
#     data = serializers.SerializerMethodField()

#     def get_data(self, obj):
#         queryset = Property.objects.all()
#         limit = self.validated_data.get('limit')
#         offset = self.validated_data.get('offset')
#         # category_limit = self.validated_data.get('limit')  # Get the category limit

#         if limit is not None and offset is not None:
#             queryset = queryset[offset:offset + limit]

#         # Get all properties, but limit the categories for each property
#         properties = PropertySerializer(queryset, many=True).data

#         # Apply the category limit
#         if limit is not None:
#             for property_data in properties:
#                 property_data['category_type'] = property_data['category_type'][:limit]

#         return properties


class PropertyListSerializer(serializers.Serializer):
    limit = serializers.IntegerField(default=10)  # Default limit of 10
    offset = serializers.IntegerField(required=False)
    data = serializers.SerializerMethodField()

    def get_data(self, obj):
        queryset = Property.objects.all()
        limit = self.validated_data.get('limit')
        offset = self.validated_data.get('offset')

        if limit is not None and offset is not None:
            queryset = queryset[offset:offset + limit]

        return PropertySerializer(queryset, many=True).data

