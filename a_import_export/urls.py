from django.urls import path, include
from .views import import_view, export_view


urlpatterns = [
    path('import/', import_view, name = "import"),
    path("export/", export_view, name = "export")
]