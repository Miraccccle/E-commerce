from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='images/users/', default='images/users/default.jpg')

    def __str__(self):
        return f'{self.user.username}'

    def user_name(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.username}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="auto" height="50px" />')
        else:
            return 'No Image'
