from rest_framework import  generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.all()

class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

