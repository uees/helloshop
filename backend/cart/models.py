from django.db import models
from django_mysql.models import Model


class Cart(Model):
    store = models.CharField(max_length=255, null=True, blank=True)
    items_count = models.IntegerField("购物车中active状态产品的总个数", default=0)
    items_all_count = models.IntegerField("购物车中全部产品的总个数", default=0)
    remote_ip = models.CharField(max_length=64, null=True, blank=True)
    coupon_code = models.CharField("优惠劵", max_length=64, null=True, blank=True)
    payment_method = models.CharField("支付方式", max_length=32, null=True, blank=True)
    shipping_method = models.CharField("货运方式", max_length=32, null=True, blank=True)
    customer_email = models.CharField(max_length=255, null=True, blank=True)
    customer_first_name = models.CharField(max_length=255, null=True, blank=True)
    customer_last_name = models.CharField(max_length=255, null=True, blank=True)
    customer_is_guest = models.BooleanField("是否游客", null=True, blank=True)
    customer_telephone = models.CharField("手机", max_length=64, null=True, blank=True)
    customer_address_country = models.CharField("国家", max_length=64, null=True, blank=True)
    customer_address_state = models.CharField("省", max_length=64, null=True, blank=True)
    customer_address_city = models.CharField("市", max_length=64, null=True, blank=True)
    customer_address_area = models.CharField("市区", max_length=64, null=True, blank=True)
    customer_address_zip = models.CharField("邮编", max_length=64, null=True, blank=True)
    customer_address_street1 = models.TextField("街道1", null=True, blank=True)
    customer_address_street2 = models.TextField("街道2", null=True, blank=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    customer_address = models.ForeignKey("customer.Address", verbose_name='地址', null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey("customer.Customer", verbose_name='顾客', null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "carts"
        verbose_name = "购物车"
        verbose_name_plural = verbose_name


class CartItem(Model):
    store = models.CharField(max_length=255, null=True, blank=True)
    qty = models.IntegerField("数量", default=0)
    active = models.BooleanField("勾选", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    sku = models.ForeignKey("product.Sku", verbose_name="产品", on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name='购物车', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "购物车项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name
