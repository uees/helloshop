from django.db import models
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django_mysql.models import JSONField, Model

User = get_user_model()


class Option(Model):
    CACHE_KEY = 'OPTIONS_CACHE'

    label = models.CharField(max_length=200)
    key = models.CharField(max_length=255, unique=True)
    value = JSONField(null=True, blank=True)
    description = models.CharField("描述", max_length=255, null=True, blank=True)
    enable = models.BooleanField("可用", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "options"
        verbose_name = '选项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label

    @classmethod
    def get(cls, key, default=None):
        options = cache.get(Option.CACHE_KEY)
        if not options:
            options = cls.set_cache()
        return options.get(key, default)

    @classmethod
    def set_cache(cls):
        enable_options = cls.objects.filter(enable=True).all()
        options = {}
        for option in enable_options:
            options[option.key] = option.value
        cache.set(Option.CACHE_KEY, options)
        return options


class Domain(Model):
    key = models.CharField(max_length=255, unique=True)  # store的domain key，譬如：www.rd-shop.com
    lang = models.CharField(max_length=32)  # store对应的语言code
    lang_name = models.CharField(max_length=32)  # store语言简码对应的文字名称，将会出现在语言切换列表中显示
    currency = models.CharField("默认货币", max_length=32)  # store对应的默认货币
    mobile_enable = models.BooleanField("移动跳转", default=False)
    # JSON 字段：进行跳转的条件： phone 代表手机，tablet 代表平板
    # {"phone":True, "tablet":False}
    mobile_condition = JSONField("跳转的条件", null=True, blank=True)
    mobile_domain = models.CharField("移动页面域名", max_length=255, null=True, blank=True)
    facebook_login_app_id = models.CharField(max_length=128, null=True, blank=True)
    facebook_login_app_secret = models.CharField(max_length=128, null=True, blank=True)
    google_login_client_id = models.CharField(max_length=200, null=True, blank=True)
    google_login_client_secret = models.CharField(max_length=128, null=True, blank=True)
    sitemap_path = models.CharField(max_length=255, null=True, blank=True)
    enable = models.BooleanField("可用", default=False)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    class Meta:
        verbose_name = '商店域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.key
