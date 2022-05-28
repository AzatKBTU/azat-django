from rest_framework import generics
from .models import Books
from .serializers import BookSerializer

class ListBook(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class ListBook(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class DetailBook(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
