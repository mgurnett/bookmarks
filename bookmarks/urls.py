from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("marks/", include("marks.urls")),
    path("admin/", admin.site.urls),
]
