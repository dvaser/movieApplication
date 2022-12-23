from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    # filter for movies panel
    list_display = ('id', 'name', 'created_date', 'isPublished')
    # filter's links
    list_display_links = ('name',)
    # filter process
    list_filter = ('created_date',)
    # edit filter
    list_editable = ('isPublished',)
    # search filter
    search_fields = ('name',)
    # list on page
    list_per_page = 30



# Register your models here.

admin.site.register(Movie, MovieAdmin)