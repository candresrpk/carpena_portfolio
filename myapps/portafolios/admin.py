from django.contrib import admin
from .models import Project, Tag, ProjectTag
# Register your models here.


@admin.register(Project)
class PortafolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    
    
@admin.register(ProjectTag)
class PortafolioTagAdmin(admin.ModelAdmin):
    list_display = ('Project', 'tag', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')