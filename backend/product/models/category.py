from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Category(Model):
    name = models.CharField(max_length=64)
    status = models.SmallIntegerField()
    slug = models.CharField(max_length=255)
    description = models.CharField(max_length=255)  # 分类描述
    menu_custom = JSONField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keywords = models.CharField(max_length=255)
    level = models.IntegerField()  # 分类等级
    filter_product_attr_selected = JSONField()  # 分类页面进行过滤的属性
    filter_product_attr_unselected = JSONField()  # 分类页面不进行过滤的属性
    show_in_menu = models.SmallIntegerField()  # 是否在菜单中显示该分类
    thumbnail_image = models.CharField(max_length=255)  # 缩略图
    image = models.CharField(max_length=255)  # 分类图
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    parent = models.ForeignKey('self', verbose_name="父亲分类", null=True, on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
