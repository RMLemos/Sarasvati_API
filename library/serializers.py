from rest_framework import serializers
from library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Author
        fields = '__all__' 

class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = '__all__' 

class BookDetailSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=True, read_only=True)

    class Meta: 
        model = Book
        fields = [
            'id_book',
            'cover',
            'title',
            'publisher',
            'nr_pages',
            'isbn',
            'synopsis',
            'author',
        ] 
