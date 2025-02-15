from django.db import models
from django_resized import ResizedImageField
from django.core.files.storage import FileSystemStorage
from backend.settings import BASE_DIR, MEDIA_ROOT
import os

# Create your models here.


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Image(models.Model):
    category = models.CharField(max_length = 256,default = 'Upload Image')
    uploads = ResizedImageField(size = [200,200], upload_to = 'uploaded_images/' , storage = OverwriteStorage())
    
    def __str__(self):
        return str(self.category)
