# Generated by Django 4.0.5 on 2022-06-07 15:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0002_alter_homeplacesale_persons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeplacesale',
            name='vat',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='categories',
            field=models.CharField(default=True, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='image',
            field=models.ImageField(upload_to='restaurants/'),
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='location',
            field=models.CharField(default=True, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='price',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='slug',
            field=models.SlugField(blank=True, default=True, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='title',
            field=models.CharField(default=True, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeplacesale',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
