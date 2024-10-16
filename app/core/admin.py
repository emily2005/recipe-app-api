"""Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define admin page for users"""
    """order them by id"""
    ordering = ['id']
    list_display = ['email', 'name']
    """useradmin needs to sypport all fields in custom model not just base
    useradmin class we are using"""
    """making custom fields that exist in models.py"""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            """classes is how we assign custom css classes in django
                "wide" makes the page cleaner and neater
            """
            'classes': ('wide)'),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
