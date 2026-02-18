from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # We map the model's read_time to the frontend's readTime
    readTime = serializers.CharField(source='read_time')
    
    # Using a MethodField to ensure the image always returns a full URL
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 
            'title', 
            'slug', 
            'category', 
            'date', 
            'image', 
            'excerpt', 
            'content', 
            'author', 
            'readTime', 
            'status'
        ]

    def get_image(self, obj):
        """
        Builds the full absolute URL for the image 
        (e.g., http://127.0.0.1:8000/media/posts/ai.png)
        """
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                # This uses the current request to determine domain and port
                return request.build_absolute_uri(obj.image.url)
            # Fallback for when request context isn't available
            return f"http://127.0.0.1:8000{obj.image.url}"
        return None