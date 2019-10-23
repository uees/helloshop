from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Sku(Model):
    """
    SKU=stock keeping unit(库存量单位)
    SKU即库存进出计量的单位， 可以是以件、盒、托盘等为单位。
    SKU是物理上不可分割的最小存货单元。
    """
    UNITS = [
        ('unit', "个"),
        ('item', "件"),
        ('Tai', "台"),
        ('box', "箱/盒"),
        ('set', "套"),
        ('m', "米"),
        ('cm', "厘米"),
        ('kg', "千克"),
        ('g', "克"),
        ('bottle', '瓶'),
    ]

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    # {"color": "red", "size": "XXL"}
    attribute = JSONField("属性")
    qty = models.IntegerField("库存数量")
    unit = models.CharField("库存单位", max_length=32, choices=UNITS, default='unit')
    price = models.DecimalField("价格", max_digits=12, decimal_places=2)
    cost_price = models.DecimalField("成本价", max_digits=12, decimal_places=2)
    special_price = models.DecimalField("优惠价", max_digits=12, decimal_places=2)
    final_price = models.DecimalField("最终价格", max_digits=12, decimal_places=2)
    image = models.TextField("产品图片")
    min_sales_qty = models.IntegerField("最小购买数")
    package_number = models.IntegerField("打包销售个数")
    remark = models.TextField("备注")
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)
    spu = models.ForeignKey("Spu", verbose_name="SPU", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'SKU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
