from django.db import models

class PropertyType(models.Model):
    name = models.CharField(max_length=100)

class CategoryType(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=100)

class Image(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')

class Property(models.Model):
    id = models.CharField(primary_key=True, max_length=15) 
    name = models.CharField(max_length=100)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    category_type = models.ManyToManyField(CategoryType)
    images = models.ManyToManyField(Image)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    total_rating = models.IntegerField()
    total_review = models.IntegerField()
