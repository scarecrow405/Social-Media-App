from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(max_length=500, blank=True)
    profile_img = models.ImageField(
        upload_to='profile_images',
        default='blank-profile-picture.png',
    )
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
