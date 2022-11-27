from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "title",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("title",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("title",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
