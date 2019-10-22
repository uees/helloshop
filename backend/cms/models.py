from django.db import models
from django.contrib.auth import get_user_model
from django_mysql.models import Model

User = get_user_model()


class Post(Model):
    """文章模型"""
    STATUS_ENABLE = 1
    STATUS_DISABLE = 2

    POST_TYPES = [
        ('article', "文章"),
        ('page', "页面"),
    ]

    type = models.CharField(max_length=32, choices=POST_TYPES)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.TextField()
    content = models.TextField()
    status = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    created_user = models.ForeignKey(User, verbose_name='创建者', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
