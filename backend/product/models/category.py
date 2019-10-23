from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Category(Model):
    name = models.CharField("名称", max_length=64)
    slug = models.CharField(max_length=255, unique=True)
    enable = models.BooleanField("可用", default=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    # [{title:title, url:url, target:target}]
    menu_custom = JSONField("自定义菜单", null=True, blank=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    level = models.IntegerField("等级", default=0)  # 分类等级
    # [attr_name1, attr_name2]
    filter_product_attr_selected = JSONField()  # 分类页面进行过滤的属性
    filter_product_attr_unselected = JSONField()  # 分类页面不进行过滤的属性
    show_in_menu = models.BooleanField("在菜单中显示", default=False)  # 是否在菜单中显示该分类
    thumbnail_image = models.CharField("缩略图", max_length=255, null=True, blank=True)  # 缩略图
    image = models.CharField("图片", max_length=255, null=True, blank=True)  # 分类图
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    parent = models.ForeignKey('self', verbose_name="父亲分类", null=True, on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)
    flats = models.ManyToManyField("Flat", verbose_name="产品", through='CategoryProductMembership')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CategoryProductMembership(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    flat = models.ForeignKey("Flat", on_delete=models.CASCADE)

    class Meta:
        db_table = "product_category_membership"
