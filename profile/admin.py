from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser',
                    'is_active', 'date_joined')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
    pass
