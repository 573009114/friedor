# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-28 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u91d1\u989d')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u65e5\u671f')),
            ],
            options={
                'db_table': 'friedor_expenditures',
            },
        ),
        migrations.CreateModel(
            name='Foodproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealname', models.CharField(default='', max_length=50, verbose_name='\u9910\u54c1\u540d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u5b9a\u4ef7')),
            ],
            options={
                'db_table': 'friedor_Foodproducts',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u91d1\u989d')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u65e5\u671f')),
                ('mealname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Foodproducts')),
            ],
            options={
                'db_table': 'friedor_incomes',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='\u59d3\u540d')),
                ('mobel', models.CharField(default='', max_length=11, verbose_name='\u624b\u673a\u53f7')),
                ('address', models.CharField(default='', max_length=50, verbose_name='\u5730\u5740')),
                ('secret', models.CharField(default='', max_length=16, verbose_name='\u5bc6\u94a5')),
            ],
            options={
                'db_table': 'friedor_members',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typed', models.CharField(default='', max_length=50, verbose_name='\u54c1\u7c7b')),
                ('dishname', models.CharField(default='', max_length=50, verbose_name='\u98df\u6750\u540d')),
                ('number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u5355\u4ef7')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u603b\u4ef7')),
            ],
            options={
                'db_table': 'friedor_Stocks',
            },
        ),
        migrations.AddField(
            model_name='expenditure',
            name='dishname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Stock'),
        ),
    ]