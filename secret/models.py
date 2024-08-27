import uuid
from django.db import models

# Create your models here.
class Secret(models.Model):
    secret = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.secret