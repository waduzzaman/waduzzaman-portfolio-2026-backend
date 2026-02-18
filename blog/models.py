from django.db import models
from django.utils.text import slugify

CATEGORY_CHOICES = [
    ("All", "All"),
    ("AI & Machine Learning", "AI & Machine Learning"),
    ("Cloud & DevOps", "Cloud & DevOps"),
    ("Cybersecurity", "Cybersecurity"),
    ("Programming", "Programming"),
    ("Blockchain & Web3", "Blockchain & Web3"),
    ("IoT & Smart Tech", "IoT & Smart Tech"),
]

STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
]

class Post(models.Model):
    title = models.CharField(max_length=200)
    # The slug field is used for Next.js URLs
    slug = models.SlugField(unique=True, max_length=250, blank=True)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="All")
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    read_time = models.CharField(max_length=50, default="5 min read")
    excerpt = models.TextField(default="")
    author = models.CharField(max_length=100, default="Admin")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def save(self, *args, **kwargs):
        # Automatically generate a slug if one doesn't exist
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title