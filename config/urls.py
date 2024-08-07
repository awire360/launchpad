from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("__debug__", include("debug_toolbar.urls")),
]
