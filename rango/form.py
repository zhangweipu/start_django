"""
定义表单类然后到view中声明
"""
from django import forms

from rango.models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # 嵌套的类，为表单提供额外的信息
    class Meta:
        # 把这个ModelForm与模型连接起来
        model = Category
        # 这是什么
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='please enter the title of page')
    url = forms.CharField(max_length=200, help_text='please enter url')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        # 排除该字段
        exclude = ('category',)
        # 包含该字段
        # fields = ('title')
