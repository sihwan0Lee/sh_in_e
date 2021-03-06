# Generated by Django 3.2 on 2021-04-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('nickname', models.CharField(max_length=30, unique='True', verbose_name='닉네임')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='메일')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('phone_number', models.CharField(max_length=30, unique=True, verbose_name='전화번호')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='등록일')),
            ],
            options={
                'verbose_name': '회원',
                'verbose_name_plural': '회원',
                'db_table': 'users',
            },
        ),
    ]
