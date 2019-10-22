from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Flat(Model):
    """产品面板"""
    name = models.CharField("名称", max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    score = models.IntegerField("评分", default=5)
    enable = models.SmallIntegerField("状态", default=True)
    qty = models.IntegerField("库存", default=0)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    price = models.DecimalField("价格", max_digits=12, decimal_places=2)
    special_from = models.DateTimeField("特价开始时间", null=True, blank=True)
    special_to = models.DateTimeField("特价结束时间", null=True, blank=True)
    special_price = models.DecimalField("优惠价", max_digits=12, decimal_places=2, default=0)
    final_price = models.DecimalField("最终价格", max_digits=12, decimal_places=2, null=True, editable=False)
    image = models.TextField("产品图片", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.CharField("简短描述", max_length=255, null=True, blank=True)
    favorites_num = models.IntegerField("收藏数", default=0)
    # sku ids
    relation_sku = JSONField("相关产品", null=True, blank=True)
    buy_also_buy_sku = JSONField("买了还买", null=True, blank=True)
    see_also_see_sku = JSONField("看了还看", null=True, blank=True)
    reviews_rate_star_average = models.IntegerField("评星平均值", default=5, editable=False)
    reviews_num = models.IntegerField("评论数", default=0, editable=False)
    # [{star1:4.5, user1:user, comment:content},]
    # reviews_rate_star_info = JSONField("评星详细", null=True, blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '产品面板'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
