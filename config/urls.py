from django.contrib import admin
from django.urls import path, include


urlpatterns = [
<<<<<<< HEAD
    path("", include("blog.urls")),
=======
>>>>>>> 3ba9fba (update codebase to bootstrap 5)
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("__debug__", include("debug_toolbar.urls")),
]
