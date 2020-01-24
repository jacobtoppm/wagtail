# Generated by Django 2.2.9 on 2020-01-24 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0046_personpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customdocument',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, related_name='custom_documents', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='customdocument',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, related_name='custom_images', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='customimage',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user'),
        ),
        migrations.AlterField(
            model_name='customimagefilepath',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, related_name='images_with_custom_file_paths', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='customimagefilepath',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user'),
        ),
    ]
