from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    class Meta:
        db_table = 'readers'

    reader = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField('Country', max_length=50)
    interests = models.CharField('Interests', max_length=200)
    bio = models.TextField('Profile', null=True, blank=True)