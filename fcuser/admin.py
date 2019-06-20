from django.contrib import admin
from .models import Fcuser
# Register your models here.


class FcuserAdmin (admin.ModelAdmin):
    list_display = ('username', 'password', 'user_email')

admin.site.register(Fcuser, FcuserAdmin)