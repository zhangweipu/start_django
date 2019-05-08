"""
存放该应用的URl
"""

from django.conf.urls import url

from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
