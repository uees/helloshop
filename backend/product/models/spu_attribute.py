from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class SpuAttribute(Model):
    # 如 "color"
    name = models.CharField("属性名", max_length=64)
    # 如 ["red", "yellow", "green"]
    data = JSONField("属性值")
    # 如 red
    default = JSONField("默认值", null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    # 如 select, checkbox, inputString, inputEmail, inputDate 等
    display_type = models.CharField("显示方式", max_length=32, default="checkbox")
    show_as_img = models.BooleanField("是否以图片的方式显示", default=False)
    is_required = models.SmallIntegerField("是否必填值", default=True)
    enable = models.BooleanField("可用", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    group = models.ForeignKey("SpuAttributeGroup", verbose_name="分组", on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'SPU属性'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
