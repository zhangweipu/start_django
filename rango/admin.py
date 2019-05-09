"""
注册模型，创建管理界面
"""
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page


class CategoryMain(admin.ModelAdmin):
    """
    自动管理界面，在输入分类名称时，自动填写别名
    """
    prepopulated_fields = {'slug': ('name',)}


# 定制管理页面
class PageMain(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


admin.site.register(Category,CategoryMain)
admin.site.register(Page, PageMain)
