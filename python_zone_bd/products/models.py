from django.db import models
from imagekit.models import ImageSpecField # type: ignore
from imagekit.processors import ResizeToFill # type: ignore

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField(max_length=100)
    delivery_time = models.IntegerField(default=5)
    price = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=False)
    images = models.ImageField(upload_to='products/')


    # Auto thumbnail version
    thumbnail = ImageSpecField(
        source='images',
        processors=[ResizeToFill(400, 400)],  # square thumbnail
        format='JPEG',
        options={'quality': 85}
    )


    def __str__(self):
        return f" {self.title} -->  {self.price}"
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"