# Generated by Django 4.2.7 on 2023-11-29 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fstr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='data',
            field=models.URLField(blank=True, null=True, verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='images',
            name='pereval',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='fstr.pereval'),
        ),
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
