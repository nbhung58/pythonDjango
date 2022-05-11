from django.contrib import admin
from .models import Choice, Questions

# Register your models here.
admin.site.register(Questions)
admin.site.register(Choice)
