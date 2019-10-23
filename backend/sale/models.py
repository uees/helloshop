from django.db import models
from django_mysql.models import Model


class Order(Model):
    status = models.SmallIntegerField("订单状态")
    store = models.CharField(max_length=255, null=True, blank=True)
    items_count = models.IntegerField("订单中产品的总个数", default=0)
    total_weight = models.DecimalField("总重量", max_digits=12, decimal_places=2, default=0)
    order_currency_code = models.CharField("当前货币", max_length=32)
    order_to_base_rate = models.DecimalField("当前货币和默认货币的比率", max_digits=12, decimal_places=2)
    # grand_total = 产品总额 + 各种费用
    grand_total = models.DecimalField("订单总额", max_digits=12, decimal_places=2)
    base_grand_total = models.DecimalField("默认货币订单总额", max_digits=12, decimal_places=2)
    subtotal = models.DecimalField("产品总额", max_digits=12, decimal_places=2)
    base_subtotal = models.DecimalField("默认货币产品总额", max_digits=12, decimal_places=2)
    subtotal_with_discount = models.DecimalField("产品总额去掉折扣", max_digits=12, decimal_places=2)
    base_subtotal_with_discount = models.DecimalField("默认货币产品总额去掉折扣", max_digits=12, decimal_places=2)
    is_changed = models.BooleanField("是否change", default=True)
    checkout_method = models.CharField("检出方式", max_length=32)  # guest，register 代表是游客还是登录客户
    customer_is_guest = models.BooleanField("是否游客", null=True, blank=True)
    customer_group = models.CharField("客户组 id", max_length=32, null=True, blank=True)
    customer_email = models.CharField(max_length=255, null=True, blank=True)
    customer_first_name = models.CharField(max_length=255, null=True, blank=True)
    customer_last_name = models.CharField(max_length=255, null=True, blank=True)
    customer_telephone = models.CharField("手机", max_length=64, null=True, blank=True)
    customer_address_country = models.CharField("国家", max_length=64, null=True, blank=True)
    customer_address_state = models.CharField("省", max_length=64, null=True, blank=True)
    customer_address_city = models.CharField("市", max_length=64, null=True, blank=True)
    customer_address_area = models.CharField("市区", max_length=64, null=True, blank=True)
    customer_address_zip = models.CharField("邮编", max_length=64, null=True, blank=True)
    customer_address_street1 = models.TextField("街道1", null=True, blank=True)
    customer_address_street2 = models.TextField("街道2", null=True, blank=True)
    remote_ip = models.CharField(max_length=64, null=True, blank=True)
    coupon_code = models.CharField("优惠劵", max_length=64, null=True, blank=True)
    payment_method = models.CharField("支付方式", max_length=32, null=True, blank=True)
    shipping_method = models.CharField("货运方式", max_length=32, null=True, blank=True)
    shipping_total = models.DecimalField("运费总额", max_digits=12, decimal_places=2, null=True)
    base_shipping_total = models.DecimalField("默认货币运费总额", max_digits=12, decimal_places=2, null=True)
    tracking_number = models.CharField("订单追踪号", max_length=128, null=True)
    tracking_company = models.CharField("快递公司", max_length=128, null=True)
    remark = models.TextField("备注", null=True)

    # Transaction 类型, 是在购物车点击支付按钮下单，还是在下单页面填写完货运地址信息下单
    txn_type = models.CharField("Transaction 类型", max_length=32, null=True, blank=True)
    # Transaction Id 支付平台唯一交易号, 通过这个可以在第三方支付平台查找订单
    txn_id = models.CharField("Transaction Id", max_length=32, null=True, blank=True)
    # payer_id 它是特定PayPal帐户的外部唯一标识符
    payer_id = models.CharField("PayPal payer id", max_length=32, null=True, blank=True)
    paypal_order_datetime = models.DateTimeField("订单创建时间", null=True, blank=True)
    ipn_track_id = models.CharField(max_length=32, null=True, blank=True)
    receiver_id = models.CharField(max_length=32, null=True, blank=True)
    verify_sign = models.CharField(max_length=32, null=True, blank=True)
    charset = models.CharField(max_length=32, null=True, blank=True)
    payment_fee = models.DecimalField("交易服务费", max_digits=12, decimal_places=2, null=True, blank=True)
    base_payment_fee = models.DecimalField("默认货币交易服务费", max_digits=12, decimal_places=2, null=True, blank=True)
    payment_type = models.CharField("交易类型", max_length=32, null=True, blank=True)
    correlation_id = models.CharField("快捷支付 correlation_id", max_length=32, null=True, blank=True)
    protection_eligibility = models.CharField("快捷支付 protection_eligibility", max_length=32, null=True, blank=True)
    protection_eligibility_type = models.CharField("快捷支付 protection_eligibility_type", max_length=255, null=True, blank=True)
    secure_merchant_account_id = models.CharField(max_length=32, null=True, blank=True)
    build = models.CharField(max_length=32, null=True, blank=True)
    # return_stock 代表订单归是否还了库存 此状态作用：用来标示 pending 订单是否释放产品库存
    return_stock = models.BooleanField(default=False)
    # payment_token 支付过程中使用的token，譬如 paypal express 支付
    payment_token = models.CharField(max_length=255, null=True, blank=True)
    # version 订单支付成功后，需要更改订单状态和扣除库存，为了防止多次执行扣除库存，进而使用版本号，默认为0，
    # 执行一次更改订单状态为 processing，则累加 1，执行完查询 version 是否为 1，如果不为 1，则说明执行过了，事务则回滚。
    version = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    customer = models.ForeignKey("customer.Customer", verbose_name='顾客', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name


class OrderItem(Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    weight = models.DecimalField("重量", max_digits=12, decimal_places=2)
    qty = models.IntegerField("数量")
    row_weight = models.DecimalField("总重量", max_digits=12, decimal_places=2)
    price = models.DecimalField("产品单价", max_digits=12, decimal_places=2)
    base_price = models.DecimalField("默认货币产品单价", max_digits=12, decimal_places=2)
    row_price = models.DecimalField("产品总价", max_digits=12, decimal_places=2)
    base_row_price = models.DecimalField("默认货币产品总价", max_digits=12, decimal_places=2)
    store = models.CharField(max_length=255, null=True, blank=True)
    product_url = models.CharField("产品 url", max_length=255)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    sku = models.ForeignKey("product.Sku", verbose_name="产品", null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey("customer.Customer", verbose_name='顾客', null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name="订单", null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "订单项目"
        verbose_name_plural = verbose_name
