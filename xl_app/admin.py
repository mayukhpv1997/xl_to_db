from django.contrib import admin
from .models import Xl_store
# Register your models here.
from import_export.admin import ImportExportModelAdmin
@admin.register(Xl_store)
class userdat(ImportExportModelAdmin):
    pass