from django.contrib import admin
from .models import ProjectBoard, Profile

admin.site.register(ProjectBoard)
admin.site.register(Profile)
# admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    
    list_display = (
        'nickname',
        'email',
        'date_joined',
    )

    list_display_links = (
        'nickname',
        'email',
    )