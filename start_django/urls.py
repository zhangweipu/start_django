"""start_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    存放应用的url
"""
from django.contrib import admin
# todo:和url的区别
from django.urls import path
from django.conf import settings
# 为了使用静态媒体文件，需要引用该库
from django.conf.urls.static import static
# 导入模块使用的包
from django.conf.urls import url
from django.conf.urls import include
# 导入模块
from rango import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 注册包中的地址，使用include
    url(r'^rango/', include('rango.urls')),
    url(r'^$', views.index, name='index'),
                  # settings 是全局的还是有被引用
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
