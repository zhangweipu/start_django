"""
存放应用的数据模型，数据实体之间的关系
"""
from django.db import models

# Create your models here.
# 必须继承Model
class Category(models.Model):
    # 声明存储字符数据的字段
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    # todo：需要声明级联关系
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    #
    # date = models.DateField()

    # 打印输出
    def __str__(self):
        return self.title
