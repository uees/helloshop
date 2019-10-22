from django.db import models
from django_mysql.models import Model


class Customer(Model):
    username = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateTimeField()
    is_subscribed = models.SmallIntegerField()
    status = models.SmallIntegerField()
    favorites_num = models.IntegerField()
    type = models.CharField(max_length=32)
    wx_session_key = models.CharField(max_length=255)
    wx_openid = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "customers"
        verbose_name = '顾客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{} . {}".format(self.first_name, self.last_name)


class Address(Model):

    class Meta:
        verbose_name = '地址'
        verbose_name_plural = verbose_name
