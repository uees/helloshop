from django.db import models
from django_mysql.models import Model


class Customer(Model):
    STATUS_OK = 1
    STATUS_ACTIVATE = 2
    STATUS_BLOCK = 3

    email = models.CharField("邮箱", max_length=255, unique=True)
    phone = models.CharField("手机", max_length=32, null=True, blank=True)
    password_hash = models.CharField(max_length=128, editable=False)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    birth_date = models.DateTimeField("生日", null=True, blank=True)
    is_subscribed = models.SmallIntegerField("是否订阅", null=True, blank=True)
    status = models.SmallIntegerField("状态", default=STATUS_ACTIVATE)
    favorites_num = models.IntegerField("收藏数", default=0)
    type = models.CharField("用户类型", max_length=32, default='default')
    wx_session_key = models.CharField(max_length=255, null=True, blank=True)
    wx_openid = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    class Meta:
        db_table = "customers"
        verbose_name = '顾客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class Address(Model):
    class Meta:
        verbose_name = '地址'
        verbose_name_plural = verbose_name
