
from django.contrib import admin
from .models import Dream
# Register your models here.

@admin.register(Dream)
class DreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'interpretation')


