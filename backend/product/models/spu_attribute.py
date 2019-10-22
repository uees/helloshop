from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class SpuAttribute(Model):
    name = models.CharField(max_length=128)
    value = JSONField("显示值")
    default = JSONField("默认值")
    description = models.CharField(max_length=255)
    display_type = models.CharField("显示方式", max_length=32)  # select ， inputString，inputEmail，inputDate等
    show_as_img = models.SmallIntegerField("是否以图片的方式显示")  # 1代表是，2代表否
    is_required = models.SmallIntegerField("是否必填值")  # 1代表是，2代表否
    status = models.SmallIntegerField("状态")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    group = models.ForeignKey("SpuAttributeGroup", verbose_name="分组", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name="父亲", null=True, on_delete=models.CASCADE)
    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)
