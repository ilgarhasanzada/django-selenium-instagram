from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Instagram(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    followers = models.CharField(max_length=20)
    following = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'instagram')
    
    def __str__(self) -> str:
        return self.username
 
