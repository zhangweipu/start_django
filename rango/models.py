"""
存放应用的数据模型，数据实体之间的关系
"""
from django.db import models
# 这里的作用是用横线替换空格
from django.template.defaultfilters import slugify
# Create your models here.
# 必须继承Model
class Category(models.Model):
    # 声明存储字符数据的字段
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    # 迁移工具
    slug = models.SlugField(default='', blank=True, unique=True)

    # 重写save方法。做迁移
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    # TODO：这是做啥用的，定义行为模型。
    class Meta:
        verbose_name_plural = 'catagories'

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
