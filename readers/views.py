from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from readers.serializers import NotesSerializer, RatingSerializer, StatusSerializer, UserBookSerializer
from readers.models import Notes, Rating, Status, UserBook


class UserBookViewSet(viewsets.ModelViewSet):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
    filterset_fields = ['title', 'isbn']
    filter_backends = [SearchFilter]
    search_fields = ['title', 'title']


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filterset_fields = ['status']


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filterset_fields = ['rating']


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    filterset_fields = ['note']