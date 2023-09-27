from django.contrib import admin
from .models import Password


class Admin(admin.ModelAdmin):
    list_display = ('user', 'address', 'password')
    list_filter = ('user',)
    search_fields = ('user__username', 'address')
    list_per_page = 25

    fieldsets = (
        ('User Info', {
            'fields': ('user',),
        }),
        ('Address and Password', {
            'fields': ('address', 'password'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('user',)
        return ()


admin.site.register(Password, Admin)
