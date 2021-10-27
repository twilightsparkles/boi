from rest_framework import serializers
from boisubDirectoryApp.models import Authors, Books, FeaturedPerson, BusinessOwners, Businesses

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'first_Name','last_Name')

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'author_id', 'description', 'author_first_Name', 'author_last_Name', 'image_url')

class BusinessesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Businesses
        fields = ('id', 'name', 'author_id', 'description', 'owner_first_Name', 'owner_last_Name', 'image_url')

class BusinessesOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessOwners
        fields = ('id', 'first_Name','last_Name', 'description', 'business_id')

class FeaturedPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedPerson
        fields = ('id', 'first_Name','last_Name', 'description', 'website_link')
