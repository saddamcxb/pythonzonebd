from django.contrib import admin
from .models import Product, ContactMessage
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", 'title', 'description', 'price', 'available']
    search_fields = ["title"]


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "created_at"]
    
