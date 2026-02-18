from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings # Add this
from django.conf.urls.static import static # Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("blog.urls")), # Keep only one of these
    path("", lambda request: HttpResponse("Welcome to the Blog API!")),
]

# This is CRITICAL for your blog images to work in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)