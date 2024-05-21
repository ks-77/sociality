from django.contrib import admin

from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number")


admin.site.register(CustomUser, CustomUserAdmin)
