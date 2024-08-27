from django.urls import path
from secret import views as secret_views

app_name = "secret"

urlpatterns = [
    path("", secret_views.index, name="index"),
    path("new/", secret_views.create_secret, name="create-secret"),
    path("return/<uuid:uuid>/", secret_views.read_secret, name="read-secret"),
]