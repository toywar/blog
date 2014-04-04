# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    class Meta():
        db_table = 'blogpost'
        ordering = ('-blogpost_date', )

    blogpost_title = models.CharField(max_length=200, verbose_name=u'Заголовок')
    blogpost_text = models.TextField(verbose_name=u'Текст')
    blogpost_date = models.DateTimeField(verbose_name=u'Дата и Время')
    blogpost_likes = models.IntegerField(default=0, verbose_name=u'Мне нравится')

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(verbose_name=u"Ваш комментарий:")
    comments_blogpost = models.ForeignKey(BlogPost)