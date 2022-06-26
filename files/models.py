from django.db import models
import uuid
from django.forms import ModelForm
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.
class File(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_file = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.uploaded_file)

class Shared(models.Model):
    files = models.ForeignKey(File, null=True, on_delete=models.CASCADE)
    share_with = models.ManyToManyField(Profile)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.share_with)
