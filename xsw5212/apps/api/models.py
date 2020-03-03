from django.db import models
from utils.models import BaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    id_choice = [(0, '普通用户'), (1, '作者')]
    tel = models.CharField(default='', max_length=32)
    qq = models.CharField(default='', max_length=32)
    identity = models.IntegerField(choices=id_choice, default=0)
    vip = models.BooleanField(default=False)

    class Meta:
        db_table = 'xsw_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Novel(BaseModel):
    name = models.CharField(max_length=128, null=True)
    introduction = models.CharField(max_length=1024)
    end = models.BooleanField(default=False)
    word_num = models.IntegerField(default=0)
    appraise_score = models.IntegerField(default=0)
    appraise_people_num = models.IntegerField(default=0)
    author = models.ForeignKey(to='User', to_field='id', related_name='novels',
                                  on_delete=models.CASCADE, db_constraint=False)
    category = models.ManyToManyField('Category')

    @property
    def appraise(self):
        return float('%.2f' % (self.appraise_score / self.appraise_people_num))

    class Meta:
        db_table = 'xsw_novel'
        verbose_name = '小说'
        verbose_name_plural = verbose_name


class Category(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'xsw_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Chapter(BaseModel):
    title = models.CharField(max_length=64)
    word_num = models.IntegerField(default=0)
    novel = models.ForeignKey(to='Novel', to_field='id', related_name='chapters',
                              on_delete=models.CASCADE, db_constraint=False)

    class Meta:
        db_table = 'xsw_chapter'
        verbose_name = '章节'
        verbose_name_plural = verbose_name
