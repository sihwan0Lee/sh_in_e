from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='이름')
    nickname = models.CharField(
        max_length=30, unique='True', default='', verbose_name='닉네임')
    email = models.EmailField(max_length=100, unique=True, verbose_name='메일')
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    phone_number = models.CharField(
        max_length=30, unique=True, verbose_name='전화번호')
    register_date = models.DateField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'users'
        verbose_name = '회원'
        verbose_name_plural = '회원'
