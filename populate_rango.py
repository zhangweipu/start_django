"""
一个填充脚本
"""
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'start_django.settings')

import django

django.setup()

from rango.models import Category, Page


def populate():
    """
    首先创建一些字典，列出想添加到各分类的网页，
    然后创建一个嵌套字典，设置各分类，
    这么做看起来不易理解，但是便于迭代，方便为模型添加数据
    :return:
    """
    python_pages = [
        {"title": "official python tutorial 1",
         "url": "http://docso.com1"},
        {"title": "official python tutorial 2",
         "url": "http://docso.com2"},
        {"title": "official python tutorial 3",
         "url": "http://docso.com3"}
    ]

    django_pages = [
        {"title": "django official python tutorial 1",
         "url": "django http://docso.com1"},
        {"title": "django official python tutorial 2",
         "url": "django http://docso.com2"},
        {"title": "django official python tutorial 3",
         "url": "django http://docso.com3"}
    ]
    other_pages = [
        {"title": "other official python tutorial 1",
         "url": "other http://docso.com1"},
        {"title": "other official python tutorial 2",
         "url": "other http://docso.com2"},
        {"title": "other official python tutorial 3",
         "url": "other http://docso.com3"}
    ]
    cats = {"python": {"pages": python_pages},
            "django": {"pages": django_pages},
            "other": {"pages": other_pages}
            }
    # 存入数据库
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
    # 读取数据
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print('{0}-{1}'.format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    """

    :param cat:
    :param titile:
    :param url:
    :param views:
    :return:
    """
    # 先查询吗？？？
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    # todo:get_or_create()会返回（object,created=true).[0]是获取object
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = random.randint(1, 10)
    c.views = 5
    c.save()
    return c


if __name__ == '__main__':
    populate()
