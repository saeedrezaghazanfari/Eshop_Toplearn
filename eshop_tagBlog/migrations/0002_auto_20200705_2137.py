# Generated by Django 3.0.7 on 2020-07-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_blog', '0001_initial'),
        ('eshop_tagBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tagblog',
            options={'verbose_name': 'برچسب خبر', 'verbose_name_plural': 'برچسب اخبار'},
        ),
        migrations.AlterField(
            model_name='tagblog',
            name='active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='tagblog',
            name='blogs',
            field=models.ManyToManyField(blank=True, to='eshop_blog.Blog', verbose_name='لیست اخبار'),
        ),
        migrations.AlterField(
            model_name='tagblog',
            name='slug',
            field=models.SlugField(verbose_name='عنوان در url'),
        ),
        migrations.AlterField(
            model_name='tagblog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان'),
        ),
        migrations.AlterField(
            model_name='tagblog',
            name='title',
            field=models.CharField(max_length=120, verbose_name='عنوان'),
        ),
    ]