from django.contrib import admin
from .models import Post
from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name',  'video']
    ordering = ['-id']
    search_fields = ['name']
    list_filter = ['first_name']
    prepopulated_fields = {
        'slug' : ('first_name',)
    }



admin.site.register(Comment)

