from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = User
        fields = '__all__' 

class ProfileSerializer(serializers.ModelSerializer):
    reader = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'country', 'interests', 'bio', 'reader']