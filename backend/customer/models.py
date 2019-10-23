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
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField("邮件地址", max_length=255, null=True, blank=True)
    company = models.CharField("公司", max_length=255, null=True, blank=True)
    telephone = models.CharField("手机", max_length=64, null=True, blank=True)
    fax = models.CharField("传真", max_length=64, null=True, blank=True)
    zip = models.CharField("邮编", max_length=64, null=True, blank=True)
    country = models.CharField("国家", max_length=64, null=True, blank=True)
    state = models.CharField("省", max_length=64, null=True, blank=True)
    city = models.CharField("市", max_length=64, null=True, blank=True)
    area = models.CharField("市区", max_length=64, null=True, blank=True)
    street1 = models.TextField("街道1", null=True, blank=True)
    street2 = models.TextField("街道2", null=True, blank=True)
    is_default = models.BooleanField("默认地址", default=False)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    customer = models.ForeignKey(Customer, verbose_name="顾客", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{country} {state} {city} {area} {street1} {street2}".format(
            country=self.country,
            state=self.state,
            city=self.city,
            area=self.area,
            street1=self.street1,
            street2=self.street2,
        )


class Favorite(Model):
    store = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    customer = models.ForeignKey(Customer, verbose_name="顾客", on_delete=models.CASCADE)
    flat = models.ForeignKey("product.Flat", verbose_name="产品", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id
