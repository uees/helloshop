from django.contrib import admin
from django.contrib.admin import widgets
from django.db import models

from .models import Post, StaticBlock


@admin.register(StaticBlock)
class StaticBlockAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('options', {
            # 'classes': ('collapse',),
            'fields': ('enable', 'identify'),
        }),
    )

    """
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        # 给当前模型 title 字段指定 widget
        if db_field.name == "title":
            kwargs['widget'] = widgets.AdminTextInputWidget
            return db_field.formfield(**kwargs)
        return super().formfield_for_dbfield(db_field, request, **kwargs)
    """


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('type', 'status',)
