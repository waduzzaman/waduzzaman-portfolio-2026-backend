from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # This is the magic line that fixes your slug issue!
    prepopulated_fields = {"slug": ("title",)}
    
    # These columns will appear in your admin list view
    list_display = ("title", "category", "status", "date", "author")
    
    # Adds a sidebar filter for easy sorting
    list_filter = ("status", "category", "date")
    
    # Allows you to search by title or content
    search_fields = ("title", "content")
    