from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_avatar.svg', upload_to='profiles')

    def __str__(self) -> str:
        return f'Profile {self.user.username}' 