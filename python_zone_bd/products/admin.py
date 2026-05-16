# admin.py
from django.contrib import admin
from .models import Product, ProductImage, ContactMessage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'pages', 'available', 'has_video_display']
    list_filter = ['available', 'technology']
    search_fields = ['title', 'description', 'technology']
    inlines = [ProductImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'technology', 'price', 'pages', 'available')
        }),
        ('Video Demo', {
            'fields': ('video_file', 'video_url', 'video_thumbnail'),
            'classes': ('wide', 'collapse',),
            'description': 'Add a video demo to help users understand your product better'
        }),
    )
    
    def has_video_display(self, obj):
        return obj.has_video()
    has_video_display.boolean = True
    has_video_display.short_description = 'Has Video Demo'

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ContactMessage)