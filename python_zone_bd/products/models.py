# models.py (updated version)
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField(max_length=100)
    pages = models.CharField(max_length=200, null=True, blank=True)
    price = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=False)
    
    # New video fields
    video_file = models.FileField(
        upload_to='product_videos/',
        null=True,
        blank=True,
        help_text="Upload MP4 video file (max 100MB)"
    )
    video_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="YouTube or Vimeo URL (e.g., https://www.youtube.com/watch?v=...)"
    )
    video_thumbnail = models.ImageField(
        upload_to='video_thumbnails/',
        null=True,
        blank=True,
        help_text="Thumbnail image for video (optional)"
    )

    def __str__(self):
        return f"{self.title} --> {self.price}"
    
    def has_video(self):
        """Check if product has any video content"""
        return bool(self.video_file or self.video_url)
    
    def get_video_embed_url(self):
        """Convert YouTube/Vimeo URLs to embed format"""
        if self.video_url:
            # YouTube handling
            if 'youtube.com' in self.video_url or 'youtu.be' in self.video_url:
                video_id = None
                if 'youtube.com/watch?v=' in self.video_url:
                    video_id = self.video_url.split('v=')[1][:11]
                elif 'youtu.be/' in self.video_url:
                    video_id = self.video_url.split('youtu.be/')[1][:11]
                elif 'youtube.com/embed/' in self.video_url:
                    video_id = self.video_url.split('embed/')[1].split('?')[0]
                
                if video_id:
                    return f'https://www.youtube.com/embed/{video_id}'
            
            # Vimeo handling
            elif 'vimeo.com' in self.video_url:
                if 'vimeo.com/' in self.video_url:
                    video_id = self.video_url.split('vimeo.com/')[1].split('?')[0]
                    return f'https://player.vimeo.com/video/{video_id}'
        
        return None


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='product_screenshots/')

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 400)],
        format='JPEG',
        options={'quality': 85}
    )

    def __str__(self):
        return f"{self.product.title} Screenshot"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"