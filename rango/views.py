"""
存放处理请求并返回响应的函数
"""
# 把上下文字典中的数据代入模板
from django.shortcuts import render
# 导入包
from rango.models import Category
from rango.models import Page

from rango.form import CategoryForm
# Create your views here.

from django.http import HttpResponse


def index(request):
    contest_dict = {'boldmessage': "这是服务器返回内容"}
    # likes是根据这个字段排序，-是倒叙的标志
    catagory_list = Category.objects.order_by('-likes')[:5]
    content_dict = {'category': catagory_list}
    return render(request, 'rango/index.html', context=content_dict)


def page(request, category_name_slug):
    print(category_name_slug + 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # 创建上下文字典，稍后传给模板渲染引擎
    context_dict = {}
    try:
        # 通过传入的别名进行查询，.get取到值会返回一个对象，没有就抛异常
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/page.html', context_dict)


def add_category(request):
    # 实例化
    form = CategoryForm()
    # 判断请求类型
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # 返回首页
            return index(request)
        else:
            print(form.errors)
    # 渲染表单，并显示可能出现的错误to html 编写页面表单
    return render(request, 'rango/page.html', {'form': form})
