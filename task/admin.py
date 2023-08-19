from django.contrib import admin
from .models import Property, PropertyType, CategoryType, Image

admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(CategoryType)
admin.site.register(Image)
