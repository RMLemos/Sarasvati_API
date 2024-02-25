from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from accounts.models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'first_name',
            'last_name', 'email', 'password'
        ]
        extra_kwargs = {
             'password': {'write_only': True}
         }
        
    def create(self, validated_data):
           validated_data['password'] = make_password(validated_data.get('password'))
           return super(UserSerializer, self).create(validated_data)
    

class ProfileSerializer(serializers.ModelSerializer):
    reader_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='reader', write_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'country', 'interests', 'bio', 'reader_id']
