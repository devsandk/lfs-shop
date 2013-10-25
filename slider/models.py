# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lfs.core.fields.thumbs import ImageWithThumbsField

# Create your models here.
class Slider(models.Model):
    title = models.CharField(_(u"Заголовок слайда"), max_length=20, blank=True)
    image=models.ImageField(_(u"Изображение"), upload_to='images', blank=True)
    description =models.TextField(_(u"Описание слайда"), max_length=180)
    href=models.CharField(_(u"Ссыдка"), max_length=250)

    def __unocode__(self):
        return self.title
