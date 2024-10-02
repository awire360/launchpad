from django.db import models
from user.models import User

def get_image_filename(instance, filename):
    class_name = instance.__class__.__name__.lower()
    id = instance.id
    return f"{class_name}/{id}/{filename}"

# Create your models here.
class Space(models.Model):
    name = models.CharField(max_length=200, help_text="This is usually your department name")
    description = models.TextField(help_text="Describe your department and what it does")
    image = models.ImageField(
        upload_to=get_image_filename, 
        default="", 
        blank=True, 
        null=True
        )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="updated_by")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to=get_image_filename, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    