from rest_framework import serializers
from .models import Books, Journal

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('name', 'price', 'description', 'created_at', 'num_pages', 'genre')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('name', 'price', 'description', 'created_at', 'num_pages', 'genre')