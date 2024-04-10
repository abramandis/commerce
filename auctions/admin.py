from django.contrib import admin
from .models import Listing, User, Bid, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_by', 'created_at')
    search_fields = ['content', 'created_by__username']
    list_filter = ('created_at',)
# Register your models here.

admin.site.register(Listing)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Comment, CommentAdmin)

