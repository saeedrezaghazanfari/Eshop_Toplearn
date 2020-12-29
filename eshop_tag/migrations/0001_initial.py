# Generated by Django 3.0.7 on 2020-06-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان برچسب')),
                ('slug', models.SlugField(verbose_name='عنوان در url')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
            ],
            options={
                'verbose_name': 'تگ/برچسب',
                'verbose_name_plural': 'تگ ها',
            },
        ),
    ]