from rest_framework import serializers
from readers.models import Notes, Rating, Status, UserBook

class UserBookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserBook
        fields = '__all__' 


class StatusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Status
        fields = '__all__' 

class RatingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rating
        fields = '__all__' 


class NotesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Notes
        fields = '__all__' 


