
# project/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rwandanRegistration.urls')),  # Include the URLs from the router
]
