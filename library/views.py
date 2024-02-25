from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from library import serializers
from library import models


class AuthorViewSet(viewsets.ModelViewSet):
       queryset = models.Author.objects.all()
       serializer_class = serializers.AuthorSerializer
       filterset_fields = ['name', 'country']
       filter_backends = [SearchFilter]
       search_fields = ['name', 'country']

class BookViewSet(viewsets.ModelViewSet):
      queryset = models.Book.objects.all()
      serializer_class = serializers.BookSerializer
      filterset_fields = ['title', 'isbn']
      filter_backends = [SearchFilter]
      search_fields = ['title', 'title']
      
      def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = serializers.BookDetailSerializer(instance)  # BookDetailSerializer to include data of the authors
        return Response(serializer.data)
