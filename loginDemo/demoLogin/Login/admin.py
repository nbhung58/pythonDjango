from ctypes.wintypes import POINT
from django.contrib import admin
from .models import Post, MyUser
# Register your models here.
admin.site.register(Post)
admin.site.register(MyUser)