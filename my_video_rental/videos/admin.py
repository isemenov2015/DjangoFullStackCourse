from django.contrib import admin
from . import models

class MovieAmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']
    search_fields = ['title', 'release_year']
    list_filter = ['release_year', 'length']
    list_display = ['title', 'release_year', 'length']
    list_editable = ['release_year', 'length']

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAmin)
