from django.db import models
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django_mysql.models import JSONField, Model

User = get_user_model()


class Option(Model):
    CACHE_KEY = 'OPTIONS_CACHE'

    name = models.CharField('项目', max_length=200)
    key = models.CharField('Key', max_length=255, unique=True)
    value = JSONField('Value', null=True, blank=True)
    description = models.CharField(max_length=255)
    enable = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "options"
        verbose_name = '选项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

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
    key = models.CharField(max_length=255)  # store的domain key，譬如：www.rd-shop.com
    lang = models.CharField(max_length=32)  # store对应的语言code
    lang_name = models.CharField(max_length=32)  # store语言简码对应的文字名称，将会出现在语言切换列表中显示
    currency = models.CharField(max_length=32)  # store对应的默认货币
    mobile_enable = models.SmallIntegerField()
    mobile_condition = JSONField()  # JSON 字段：进行跳转的条件：phone 代表手机，tablet代表平板，当都填写，代表手机和平板都会进行跳转
    mobile_domain = models.CharField(max_length=255)
    facebook_login_app_id = models.CharField(max_length=128)
    facebook_login_app_secret = models.CharField(max_length=128)
    google_login_client_id = models.CharField(max_length=200)
    google_login_client_secret = models.CharField(max_length=128)
    sitemap_path = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        verbose_name = '商店域'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.key
