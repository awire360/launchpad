from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


def get_image_filename(instance, filename):
    class_name = instance.__class__.__name__.lower()
    id = instance.id
    return f"{class_name}/{id}/{filename}"


class User(AbstractUser):

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = CountryField(blank=True, blank_label="select country")
    avatar = models.ImageField(upload_to=get_image_filename, blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
