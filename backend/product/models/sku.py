from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Sku(Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    status = models.SmallIntegerField("状态")
    qty = models.IntegerField("库存")
    price = models.DecimalField("价格", max_digits=12, decimal_places=2)
    cost_price = models.DecimalField("成本价", max_digits=12, decimal_places=2)
    special_price = models.DecimalField("优惠价", max_digits=12, decimal_places=2)
    special_from = models.DateTimeField("特价开始时间")
    special_to = models.DateTimeField("特价结束时间")
    final_price = models.DecimalField("最终价格", max_digits=12, decimal_places=2)
    new_product_from = models.DateTimeField()
    new_product_to = models.DateTimeField()
    image = models.TextField("产品图片")
    long = models.IntegerField("产品的长度")
    width = models.IntegerField("产品的宽度")
    height = models.IntegerField("产品的高度")
    weight = models.DecimalField("重量", max_digits=11, decimal_places=2)
    volume_weight = models.DecimalField("体积重", max_digits=11, decimal_places=2)
    package_number = models.IntegerField("打包销售个数")
    spu = models.ForeignKey("Spu", verbose_name="SPU", on_delete=models.CASCADE)
