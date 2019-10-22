from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model, JSONField

User = get_user_model()


class SpuAttributeGroup(Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    status = models.SmallIntegerField("状态")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)
