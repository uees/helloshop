from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model

User = get_user_model()


class Review(Model):
    STATUS_PUBLISH = 1
    STATUS_AUDIT = 2
    POST_STATUS = [
        (STATUS_PUBLISH, "发布"),
        (STATUS_AUDIT, "待审核"),
    ]

    name = models.CharField("评论人姓名", max_length=32, editable=False)
    ip = models.CharField(max_length=64, null=True, editable=False)
    user_agent = models.CharField(max_length=255, null=True, editable=False)
    content = models.TextField("内容", null=True, blank=True)
    rate_star = models.SmallIntegerField("评星", default=5)
    store = models.CharField("商店", max_length=128, null=True, blank=True)
    lang_code = models.CharField("语言简码", max_length=32)
    status = models.SmallIntegerField("状态", default=STATUS_PUBLISH)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)
    audit_at = models.DateTimeField("审核时间", null=True, editable=False)

    audit_user = models.ForeignKey(User, verbose_name="审核用户", on_delete=models.SET_NULL)
    sku = models.ForeignKey("Sku", verbose_name="SKU", on_delete=models.SET_NULL)
    flat = models.ForeignKey("Flat", verbose_name="产品", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", verbose_name="客户", on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{} {}star".format(self.name, self.rate_star)
