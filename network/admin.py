from django.contrib import admin

from .models import User, Posts

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('username',)
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'date_joined',)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'created')
    ordering = ('-created',)
    search_fields = ('text', 'author')
    list_filter = ('author', 'likes',)


admin.site.register(User, UserAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.site_header = "Network Site Administration"
