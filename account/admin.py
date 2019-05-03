from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


class ProfileInLine(admin.StackedInline):
    model = Profile


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInLine, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
