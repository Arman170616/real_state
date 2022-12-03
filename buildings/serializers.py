from rest_framework import serializers
from .models import Home, ImageFiles

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('title', 'slug', 'photo', 'bathrooms', 'sqrt', 'address', 'zipcode', 'city', 'description', 'sale_type', 'home_type', 'price', 'bedrooms', 'open_house','is_published')


class HomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        lookup_field = 'slug'


class ImageFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFiles
        fields = '__all__'
        lookup_field = 'home'
