from django.contrib import admin

from ramailo.models.feedback import Feedback
from ramailo.models.notification import FCMDevice
from ramailo.models.user import User
from ramailo.models.blog.post import Post
from ramailo.models.blog.category import Category


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'idx', 'mobile', 'name', 'position', 'created_at']
    search_fields = ['name', 'mobile']
    list_filter = ['is_approved', 'is_email_verified', 'is_kyc_verified']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'is_published', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['is_published', 'created_at', 'category']
    filter_horizontal = ['category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

admin.site.register(FCMDevice)
