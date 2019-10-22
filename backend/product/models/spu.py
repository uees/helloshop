from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class Spu(Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    status = models.SmallIntegerField("状态")

    attribute_group = models.ForeignKey("SpuAttributeGroup", verbose_name="属性组", on_delete=models.SET_NULL, null=True)
    flat = models.ForeignKey("Flat", verbose_name="海报", on_delete=models.SET_NULL, null=True)
