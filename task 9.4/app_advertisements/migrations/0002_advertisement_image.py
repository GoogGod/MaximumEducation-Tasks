# Generated by Django 4.2.3 on 2023-08-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='1', upload_to='advertisements/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
