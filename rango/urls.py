"""
存放该应用的URl
"""

from django.conf.urls import url

from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^about/$')
    # 变量要一致
    url(r'^page/(?P<category_name_slug>[\w\-]+)/$', views.page, name='page'),
    url(r'^add_category/$', views.add_category, name='category')
]
