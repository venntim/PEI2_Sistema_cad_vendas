from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("vendas/", include("vendas.urls")),
    path("", include("vendas.urls")),
]
