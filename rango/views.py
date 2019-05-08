"""
存放处理请求并返回响应的函数
"""
# 把上下文字典中的数据代入模板
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    contest_dict = {'boldmessage': "这是服务器返回内容"}
    return render(request, 'rango/index.html', context=contest_dict)
