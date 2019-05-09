"""
WSGI config for start_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
用于运行开发服务器和把项目部署到生产环境的python脚本
"""

import os

from django.core.wsgi import get_wsgi_application
# 加载框架的环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'start_django.settings')

application = get_wsgi_application()
