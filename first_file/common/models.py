from django.db import models
from django_resized import ResizedImageField

class Gallery(models.Model):
    title = models.CharField(max_length=256)
    Image = ResizedImageField (size = [1200, 800], crop = ['middle', 'center'], quality=95, upload_to="gallery/%Y/%m")

    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        db_table = "gallery"
        verbose_name = "gallery"
        verbose_name_plural = "gallery"

class Cars(models.Model):
    title = models.CharField(max_length=256)
    image = ResizedImageField (size = [1200, 800], crop = ['middle', 'center'], quality=95, upload_to="cars/%Y/%m")

    def __str__(self) -> str:
        return f"Beautifull Butterfly Car{self.title}"
    
    class CarsMeta:
        db_table = "cars"
        verbose_name = "cars"
        verbose_name_plural = "cars"

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=64)
    subject = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        db_table = "contact"
        verbose_name = "contact"
        verbose_name_plural = "contacts"

class Video(models.Model):
    video = models.FileField(upload_to='video/',blank=True,null=True)
        
    def __str__(self) -> str:
        return f"{self.video}"

    class VideoMeta:
        db_table = "video"
        verbose_name = "video"
        verbose_name_plural = "videos" 
    