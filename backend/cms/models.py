from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model

User = get_user_model()


class Post(Model):
    """文章模型"""
    POST_TYPES = [
        ('article', "文章"),
        ('page', "页面"),
    ]

    STATUS_PUBLISH = 1
    STATUS_DRAFT = 2
    STATUS_AUDIT = 3
    POST_STATUS = [
        (STATUS_PUBLISH, "发布"),
        (STATUS_DRAFT, "草稿"),
        (STATUS_AUDIT, "待审核"),
    ]

    type = models.CharField("类型", max_length=32, choices=POST_TYPES, default="article")
    title = models.CharField("标题", max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    content = models.TextField("内容")
    status = models.SmallIntegerField("状态", choices=POST_STATUS, default=STATUS_AUDIT)
    updated_user_id = models.IntegerField("修改者 ID", default=0)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class StaticBlock(Model):
    identify = models.CharField(max_length=100, null=True, blank=True)
    title = models.TextField()
    enable = models.BooleanField(default=True)
    content = models.TextField()
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True, null=True)

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
