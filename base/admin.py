from django.contrib import admin
from .models import Task


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'complete', 'created_at', 'user')
    list_display_links = ('id', 'title')
    list_editable = ('complete', )
    ordering = ['created_at', 'title']
    search_fields = ['title']

