# Generated by Django 3.0.7 on 2020-08-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='نام سایت')),
                ('address', models.CharField(max_length=120, verbose_name='آدرس')),
                ('phone', models.CharField(max_length=120, verbose_name='تلفن تماس')),
                ('fax', models.CharField(max_length=120, verbose_name='فکس')),
                ('email', models.CharField(max_length=120, verbose_name='ایمیل')),
                ('aboutus', models.TextField(verbose_name='درباره ما')),
                ('logo', models.ImageField(upload_to='', verbose_name='لوگو ی سایت')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیریت تنظیمات سایت',
            },
        ),
    ]