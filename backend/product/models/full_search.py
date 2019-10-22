from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model

User = get_user_model()


class FullSearch(Model):
    name = models.CharField("品名", max_length=255)
    lang = models.CharField("语言简码", max_length=32)
    product_id = models.IntegerField("产品 ID")
    spu = models.CharField("SPU", max_length=128)
    sku = models.CharField("SKU", max_length=128)
    score = models.IntegerField("产品分值")
    status = models.IntegerField("产品状态")
    has_stock = models.SmallIntegerField("产品库存状态")
    price = models.DecimalField("价格", max_digits=12, decimal_places=2)
    cost_price = models.DecimalField("成本价", max_digits=12, decimal_places=2)
    special_price = models.DecimalField("优惠价", max_digits=12, decimal_places=2)
    special_from = models.DateTimeField("特价开始时间")
    special_to = models.DateTimeField("特价结束时间")
    final_price = models.DecimalField("最终价格", max_digits=12, decimal_places=2)
    image = models.TextField("产品图片")
    short_description = models.CharField("简短描述", max_length=255)
    description = models.TextField("描述")
    created_at = models.DateTimeField("创建时间")
    sync_updated_at = models.DateTimeField("同步时间")

    class Meta:
        verbose_name = '产品查询集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
