# Generated by Django 2.0.7 on 2018-09-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookphone', '0009_auto_20180905_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_unidad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fotos', verbose_name='FOTO'),
        ),
    ]
