from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class SpuAttributeGroup(Model):
    """
    不同类型的产品有不同的属性
    例如衣服有 颜色、尺码 属性，而计算机有内存、CPU、显示器属性
    """
    name = models.CharField("组名", max_length=128)
    description = models.CharField("描述", max_length=255, null=True, blank=True)
    enable = models.SmallIntegerField("状态", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'SPU属性组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
