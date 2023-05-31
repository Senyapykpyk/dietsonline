from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import SiteUser

class SiteUserAdmin(UserAdmin):
     list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_consultant',
        
        )
     fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_consultant',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ()
        })
    )
     add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_consultant',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_consultant')
        })
    )

admin.site.register(SiteUser, SiteUserAdmin)