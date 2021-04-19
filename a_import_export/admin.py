from django.contrib import admin
from .models import ImportLog, ImportCSV


admin.site.register(ImportLog)
admin.site.register(ImportCSV)
