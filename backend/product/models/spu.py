from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Spu(Model):
    """
    SPU = Standard Product Unit （标准产品单位）
    通俗点讲，属性值、特性相同的商品就可以称为一个SPU。
    例如： iphone4就是一个SPU，与商家，与颜色、款式、套餐都无关。
    """
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    qty = models.IntegerField("库存数量")
    image = models.TextField("产品图片", null=True, blank=True)
    long = models.IntegerField("产品的长度")
    width = models.IntegerField("产品的宽度")
    height = models.IntegerField("产品的高度")
    weight = models.DecimalField("重量", max_digits=11, decimal_places=2)
    volume_weight = models.DecimalField("体积重", max_digits=11, decimal_places=2)
    attribute_info = JSONField("属性以及值")
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    attribute_group = models.ForeignKey("SpuAttributeGroup", verbose_name="属性组", on_delete=models.SET_NULL, null=True)
    flat = models.ForeignKey("Flat", verbose_name="海报", on_delete=models.SET_NULL, null=True)
    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'SPU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
