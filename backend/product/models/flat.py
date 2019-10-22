from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Flat(Model):
    """产品海报"""
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    score = models.IntegerField("评分")
    status = models.SmallIntegerField("状态")
    qty = models.IntegerField("库存")
    min_sales_qty = models.IntegerField("最小购买数")
    has_stock = models.SmallIntegerField("库存状态")  # 1代表有库存，2代表无库存
    meta_title = models.CharField(max_length=255)
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.TextField()
    price = models.DecimalField("价格", max_digits=12, decimal_places=2)
    cost_price = models.DecimalField("成本价", max_digits=12, decimal_places=2)
    special_price = models.DecimalField("优惠价", max_digits=12, decimal_places=2)
    special_from = models.DateTimeField("特价开始时间")
    special_to = models.DateTimeField("特价结束时间")
    tier_price = JSONField()
    final_price = models.DecimalField("最终价格", max_digits=12, decimal_places=2)
    new_product_from = models.DateTimeField()
    new_product_to = models.DateTimeField()
    image = models.TextField("产品图片")
    description = models.TextField()
    custom_option = JSONField()
    remark = models.TextField("备注")
    long = models.IntegerField("产品的长度")
    width = models.IntegerField("产品的宽度")
    height = models.IntegerField("产品的高度")
    weight = models.DecimalField("重量", max_digits=11, decimal_places=2)
    volume_weight = models.DecimalField("体积重", max_digits=11, decimal_places=2)
    package_number = models.IntegerField("打包销售个数")
    favorites_num = models.IntegerField("收藏数")
    relation_sku = JSONField("相关产品")
    buy_also_buy_sku = JSONField("买了还买")
    see_also_see_sku = JSONField("看了还看")
    attr_group = JSONField("属性组")
    attr_group_info = JSONField("属性组对应的属性以及值")
    reviews_rate_star_average = models.IntegerField("评星平均值")
    reviews_num = models.IntegerField("评论数")
    reviews_rate_star_average_lang = JSONField("评星平均值（语言）")
    reviews_num_lang = JSONField("评论数（语言）")
    reviews_rate_star_info = JSONField("评星详细")
    reviews_rate_star_info_lang = JSONField("评星详细（语言）")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '产品查询集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
